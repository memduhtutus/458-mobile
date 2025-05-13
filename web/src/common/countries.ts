import countries from '@/assets/countries.json'

export type TCountry = {
  name: string
  code: string
}

export const getCountryName = (code: string) => {
  return countries.find((country) => country.code === code)?.name
}

export const getCountryCode = (name: string) => {
  return countries.find((country) => country.name === name)?.code
}

export default countries as TCountry[]
