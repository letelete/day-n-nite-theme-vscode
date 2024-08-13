(async () => {
  // Extracts vscode color definitions from https://themes.vscode.one
  const definitions = await getDefinitions();
  if (definitions !== null) {
    try {
      const config = transformToDefinitionsConfig(definitions);
      outputConfig(config);
    } catch (error) {
      console.error('Error when generating config from definitions.', error);
    }
  } else {
    console.info('Definitions missing. Exiting...');
  }

  async function getDefinitions() {
    const scrapper = new Scrapper();
    try {
      return await scrapper.extractDefinitions();
    } catch (error) {
      console.error('Error when extracting definitions.', error);
    }
    return null;
  }

  function transformToDefinitionsConfig(definitions) {
    return definitions
      .reduce((lines, group, index) => {
        const { name, components } = group;

        lines.push(`#${name}`);
        Object.entries(components).forEach((component) => {
          const [key, value] = component;
          lines.push(`"${key}": "${value}",`);
        });

        const shouldAddNewLine = index === definitions.length - 1;
        if (shouldAddNewLine) {
          lines.push('');
        }

        return lines;
      }, [])
      .join('\n');
  }

  function outputConfig(config) {
    console.log(config);
  }

  function Scrapper() {
    function expandAllSettingGroups() {
      document
        .querySelectorAll('.setting-group:not(.expanded) .header.noselect')
        .forEach((e) => e.click());
    }

    function extractExpandedDefinitions() {
      return [...document.querySelectorAll('.setting-group.expanded')].map(
        (settingGroup) => {
          const name = settingGroup.querySelector(
            '.header.noselect .name span:not(.count-badge)'
          ).textContent;
          const components = Object.fromEntries(
            [...settingGroup.querySelectorAll('.setting')].map((setting) => {
              const info = setting.querySelector('.color-info');
              const key = info.querySelector('.name').textContent;
              const value = info.querySelector('.code').textContent;
              return [key, value];
            })
          );
          return { name, components };
        }
      );
    }

    async function extractDefinitions() {
      expandAllSettingGroups();

      await wait(0);
      return extractExpandedDefinitions();
    }

    return { extractDefinitions };
  }

  function wait(delay) {
    return new Promise((r) => setTimeout(r, delay));
  }
})();
