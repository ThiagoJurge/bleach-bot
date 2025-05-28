import supabase from "./src/utils/supabaseClient.js"

const { data, error } = await supabase
  .from('comandos')
  .select()

if (error) {
  console.error('Erro ao buscar comandos:', error)
} else {
  console.log('Comandos:', data)
}
