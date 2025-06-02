/**
 * Gera o menu formatado com base nos comandos.
 *
 * @param {string} groupId - ID do grupo atual.
 * @param {Array} comandos - Lista de comandos do Supabase.
 * @param {Object} [options]
 * @param {string[]} [options.excluirCategorias] - Categorias a excluir.
 * @param {string[]} [options.incluirSomenteCategorias] - Categorias a incluir exclusivamente.
 * @returns {string} menu formatado
 */
export default async function gerarMenu(groupId, comandos, options = {}) {
  const { excluirCategorias = [], incluirSomenteCategorias = [] } = options;

  // Agrupar por categoria
  const categorias = {};
  for (const cmd of comandos) {
    if (!cmd.command) continue;
    const categoria = cmd.categoria?.toLowerCase() || "outros";
    if (!categorias[categoria]) categorias[categoria] = [];
    categorias[categoria].push(cmd);
  }

  // Construir menu
  let menu = "*_░ി❁⭝ Comandos*\n\n";

  for (const cat in categorias) {
    const catLower = cat.toLowerCase();

    // Aplicar filtros
    if (
      (incluirSomenteCategorias.length && !incluirSomenteCategorias.includes(catLower)) ||
      excluirCategorias.includes(catLower)
    ) {
      continue;
    }

    const comandosDaCategoria = categorias[cat]
      .map(c => `- /${c.command}${c.title ? ` - ${c.title}` : ""}`)
      .join("\n");

    const catFormatada = cat.charAt(0).toUpperCase() + cat.slice(1);
    menu += `▚ׁ̣۬❏̷̸ⷢ♔͎┄  ${catFormatada}\n${comandosDaCategoria}\n\n`;
  }

  return menu.trim();
}
