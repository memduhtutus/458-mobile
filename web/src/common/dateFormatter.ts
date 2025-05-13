import { format } from 'date-fns'

export const formatDateToDisplay = (timestamp: number): string => {
  return format(new Date(timestamp), 'dd/MM/yyyy HH:mm')
}
