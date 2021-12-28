`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:07:16
// Design Name: 
// Module Name: encoder_wo
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module encoder_wo(out_y, in_a);
input [3:0]in_a;
output reg [1:0]out_y;
always@(in_a)
    begin
        case(in_a)
            4'b0001:out_y = 2'b00;
            4'b0010:out_y = 2'b01;
            4'b0100:out_y = 2'b10;
            4'b1000:out_y = 2'b11;
        default:$display("Error!");
    endcase
    end
endmodule