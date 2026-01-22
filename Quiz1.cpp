//
// Created by Murilo Matos on 1/22/26.
//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
///For simplicity we will make a 2d array with a couple of book titles, also used for testing

string booktable[2][2] = {
    {"wizard of oz", "the man and the sea"}, {
        "hunger games", "lola"}};

template <typename T, int col, int row>
vector<T> convert_2d_to_1d(const T (&booktable)[row][col]) {
    vector<T> result;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            const string &current = booktable[i][j];

            if(find(result.begin(), result.end(), current) == result.end()){

                result.push_back(booktable[i][j]);
            }

            //Check if this is already in the array or not
        }
    }
    return result;
}


int main() {
    string booktable[2][2] = {
        {"wizard of oz", "the man and the sea"},
        {"hunger games", "lola"}
    };

    vector<string> uniquebooks = convert_2d_to_1d(booktable);

    cout << "Unique books:\n";
    for (const auto& s : uniquebooks) {
        cout << s << "\n";
    }

    cout << "\nAll books (2D array):\n";
    for (const auto& row : booktable) {
        for (const auto& s : row) {
            cout << s << "\n";
        }
    }
}
