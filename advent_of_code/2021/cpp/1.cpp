#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream infile("../inputs/1_task.txt");
    if (!infile) {
        std::cerr << "Error opening file.";
        return 1;
    }

    std::vector<int> numbers;
    int value;
    while (infile >> value) {
        numbers.push_back(value);
    }
    infile.close();

    //std::cout << "Read " << numbers.size() << " numbers: ";
    //for (size_t i = 0; i < numbers.size(); ++i) {
        //std::cout << numbers[i];
        //if (i + 1 < numbers.size())
            //std::cout << ", ";
    //}
    std::cout << std::endl;

    // Compute and print differences between successive elements
    int ans1 = 0;

    if (numbers.size() > 1) {
        //std::cout << "Differences between successive numbers:\n";
        for (size_t i = 1; i < numbers.size(); ++i) {
            int diff = numbers[i] - numbers[i - 1];
            //std::cout << diff;
            if (diff > 0) {
                ans1++;
            }
            //if (i + 1 < numbers.size())
               // std::cout << ", ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "Not enough numbers to compute differences.\n";
    }

    std::cout << "Part 1 answer: " << ans1 <<".";

    // Compute and print differences between successive elements
    int ans2 = 0;
    if (numbers.size() > 1) {
        //std::cout << "Differences between successive numbers:\n";
        for (size_t i = 3; i < numbers.size(); ++i) {
            int term1 = numbers[i]+numbers[i-1]+numbers[i-2];
            int term2 = numbers[i - 1]+numbers[i - 2]+numbers[i - 3];
            int diff = term1 - term2;
            //std::cout << diff;
            if (diff > 0) {
                ans2++;
            }
            //if (i + 1 < numbers.size())
                //std::cout << ", ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "Not enough numbers to compute differences.\n";
    }

    std::cout << "Part 2 answer: " << ans2 <<".";

    return 0;
}
