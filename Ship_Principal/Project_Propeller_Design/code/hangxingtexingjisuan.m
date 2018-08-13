J102=[0.607170003,	0.63608286,	0.664995717, 0.693908575, 0.722821432];
J95=[0.651908845,	0.682952123,	0.713995402,	0.74503868,	0.776081959];
J85=[0.728604003,	0.763299432,	0.797994861,	0.83269029,	0.867385718];

KT102=zeros(1,5);
KQ102=zeros(1,5);
KT95=zeros(1,5);
KQ95=zeros(1,5);
KT85=zeros(1,5);
KQ85=zeros(1,5);
for i=1:5
    [kt102, kq102]=calKtKq(J102(i),0.7145,0.9364);
    KT102(i)=kt102;
    KQ102(i)=kq102;
    [kt95, kq95]=calKtKq(J95(i),0.7145,0.9364);
    KT95(i)=kt95;
    KQ95(i)=kq95;
    [kt85, kq85]=calKtKq(J85(i),0.7145,0.9364);
    KT85(i)=kt85;
    KQ85(i)=kq85;
end

Vs=[21,22,23,24,25];
[PE1, PE2, PE3] = calPE(Vs);