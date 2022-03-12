#include <string>
#include <iostream>

int main()
{
	int roomNumber = 0;
	int validRoomNumberCounter = 0;
	
	while(1)
	{
		std::string roomNumberString(std::to_string(roomNumber));
				
		if((roomNumberString.find('5') != std::string::npos) &&
		(roomNumberString.find('7') != std::string::npos))
		{
		    roomNumber++;
			continue;
		}
		else if((roomNumberString.find('5') != std::string::npos) ||
				(roomNumberString.find('7') != std::string::npos))
		{
			validRoomNumberCounter++;
			
			if(validRoomNumberCounter == 1000)
			{
				std::cout << roomNumberString << std::endl;
				break;
			}
		}
		
		roomNumber++;
	}
	
	return 0;
}
