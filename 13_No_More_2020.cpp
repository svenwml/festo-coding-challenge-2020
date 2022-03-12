#include <string>
#include <iostream>

int main()
{
	int roomNumber = 1;
	int validRoomNumberCounter = 0;
	
	while(1)
	{
		std::string roomnumberString(std::to_string(roomNumber));
				
		// Verify the room number
		size_t pos = roomnumberString.find('2');	
		
		if(pos == std::string::npos)
		{
			goto valid;
		}			
		
		pos = roomnumberString.find('0', pos + 1);
		
		if(pos == std::string::npos)
		{
			goto valid;
		}	
		
		pos = roomnumberString.find('2', pos + 1);
		
		if(pos == std::string::npos)
		{
			goto valid;
		}	
		
		pos = roomnumberString.find('0', pos + 1);
		
		if(pos != std::string::npos)
		{
		    roomNumber++;
			continue;
		}

		valid:
		
		validRoomNumberCounter++;
						
		if(validRoomNumberCounter == 1000000)
		{
			std::cout << roomnumberString << std::endl;
			break;
		}
		
		roomNumber++;
	}
		
	return 0;
}
