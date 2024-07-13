from pandas.core.frame import DataFrame
from pandas import read_csv as pd_read_csv
from json import load, dump, JSONDecodeError

class ReadUpdateFiles:
    def read_csv_emails(self, emails_csv_file_path: str) -> DataFrame:
        '''
        UseCase:
        ---
        Read CSV file of Emails and Returns Pandas's module DataFrame of given file. Also raise Exceptions.

        Args:
        ---
        - `emails_csv_file_path: str` -> File path of CSV which contain Emails in below csv format:

        ```csv
            name,email
            Saadullah Khan,SaadForContac@gmail.com
        ```
        Returns:
        ---
        > Pandas DataFrame of Readed file.
        '''
        try:
            return pd_read_csv(emails_csv_file_path)

        except FileNotFoundError:
            raise FileNotFoundError("~"*40 + "\n" + f"Given emails file path is not exists \n>> Given Path: {emails_csv_file_path}" + "\n" + "~"*50)
        
        except PermissionError:
            raise PermissionError("~"*40 + f"This Program may not have sufficient access in your given emails file path \n>> Given Path: {emails_csv_file_path}" + "\n" + "~"*50)
        
        except Exception as e:
            raise Exception("~"*45 + "\n" + f"Unexpected Error Occured When fetching emails from CSV! \nGiven Path: {emails_csv_file_path} \nError: {e}" + "\n" + "~"*50)


    def read_json_quotes(self, quotes_json_file_path: str) -> dict:
        '''
        UseCase:
        ---
        Read JSON file of Quotes and Returns Dictionary of quotes file. Also raise Exceptions.

        Args:
        ---
        - `quotes_json_file_path: str` -> File path of JSON which contain quotes in below json format:

        ```json
        {
            "last_send_quote_index": 0,
            "QUOTES": [
                ["Allama Iqbal.", "نا امیدی گناہ کبیرہ ہے"],
                ["Ashfaq Ahmed.","کامیابی کے لیے خواہش اور جنون ضروری ہے"],
                ["UnKnown.","زندگی کو سمجھنا ہے تو پیچھے دیکھو اور زندگی کو جینا ہے تو آگے دیکھو"]
            ]
        }
        ```
        Returns:
        ---
        > Dictionary of Readed quotes file.
        '''
        try:
            with open(quotes_json_file_path, "r") as f:
                return load(f)
        
        except JSONDecodeError:
            raise JSONDecodeError("~"*40 + "\n" + f"Wrong JSON syntax or File is empty. \n>> Given Path: {quotes_json_file_path}" + "\n" + "~"*50)

        except FileNotFoundError:
            raise FileNotFoundError("~"*40 + "\n" + f"Given quotes csv file path is not exists \n>> Given Path: {quotes_json_file_path}" + "\n" + "~"*50)

        except PermissionError:
            raise PermissionError("~"*40 + f"This Program may not have sufficient access in your given quotes csv file path \n>> Given Path: {quotes_json_file_path}" + "\n" + "~"*50)
        
        except Exception as e:
            raise Exception("~"*45 + "\n" + f"Unexpected Error Occured When fetching quotes from JSON!  \nGiven Path: {quotes_json_file_path} \nError: {e}" + "\n" + "~"*50)


    def extract_quote_and_update_last_sent_quote_index(self, quotes_json_file_path: str, readed_quotes_dict: dict) -> tuple[str,str]:
        '''
        UseCase:
        ---
        Extract one Quote based on last send quote index. Then Update the last sent quote index, if all quotes are sent then index will be set to 0.

        Args:
        ---
        - `quotes_json_file_path: str` -> Same path when pass to reading function as it update that file.
        - `readed_quotes_dict: dict` -> Dictionary get when file read.

        Returns:
        ---
        `tuple: str` -> (Author, Quote)
        '''
        quote_list: list = readed_quotes_dict["QUOTES"]
        last_sent_quote_index: int = readed_quotes_dict["last_send_quote_index"]

        # Updating last sent quote no, if all quote are sent then, 0 will be set
        if (len(quote_list) - 1)  > last_sent_quote_index:
            readed_quotes_dict["last_send_quote_index"] += 1
            last_sent_quote_index += 1
        else:
            readed_quotes_dict["last_send_quote_index"] = 0
            last_sent_quote_index = 0
        
        # Extracting the quote
        author, quote = quote_list[last_sent_quote_index]     # Returns Value

        # Writig to the File
        with open(quotes_json_file_path, "w") as f:
            dump(readed_quotes_dict, f, indent=4)

        return (author, quote)
