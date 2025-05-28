import fs from 'fs'
import supabase from './src/utils/supabaseClient.js'

// Lê o arquivo JSON
const raw = fs.readFileSync('./commands.json', 'utf-8')
const comandos = JSON.parse(raw)

for (const comando of comandos) {
    const { data, error } = await supabase
        .from('comandos')
        .insert([comando])

    if (error) {
        console.error(`Erro ao inserir "${comando.command}":`, error)
    } else {
        console.log(`✅ Inserido: "${comando.command}"`)
    }
}
