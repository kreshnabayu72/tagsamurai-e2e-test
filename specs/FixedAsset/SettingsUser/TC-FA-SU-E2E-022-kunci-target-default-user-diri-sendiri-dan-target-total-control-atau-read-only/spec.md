---
id: TC-FA-SU-E2E-022-kunci-target-default-user-diri-sendiri-dan-target-total-control-atau-read-only
title: "Kunci Target: Default User, Diri Sendiri, dan Target Total Control atau Read Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-70
  - TC-FA-SU-71
  - TC-FA-SU-72
coverage:
  web: automated
---

# Kunci Target: Default User, Diri Sendiri, dan Target Total Control atau Read Only

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Lina Marlina, Pre-setup #1, akun default suite); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control. Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Manage global user & role (Update) | #4 | Qori Akbar | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Group Manager (IT Infrastructure dan Accounts Payable) | #9 | Oscar Pranata | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_GM_PASSWORD` |

- Nama env `FA_MURG_UPD_PASSWORD` dan `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Target kunci: Default User (Ahmad Dahlan, Pre-setup #2, TC-FA-SU-70); akun sendiri (TC-FA-SU-71); target tier Total Control (Lina Marlina) dan Read Only (Citra Lestari) bagi aktor Manage global user & role (TC-FA-SU-72).
- Tabel "Target tier" (TC-FA-SU-72, langkah 50 sampai 63): Lina Marlina (Total Control), Citra Lestari (Read Only).
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20), tier dan penugasan (#23).
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen.
- State global: tidak ada yang diubah; data Pre-setup tidak diubah.

## Test Steps

### TC-FA-SU-70: Target Default User, seluruh kontrol tulis terkunci permanen bagi semua aktor

1. Ketik Search `Ahmad Dahlan`, tekan Enter
2. Hover sakelar Active baris Ahmad Dahlan
3. Verifikasi sakelar Active ON Disabled dengan tooltip `Default User cannot be modified.`
4. Verifikasi checkbox baris Ahmad Dahlan Disabled
5. Verifikasi Table Tools User List tampil
6. Buka row action menu `⋯` baris Ahmad Dahlan
7. Verifikasi row action `Edit Home Group` Hidden
8. Tutup row action menu dengan menekan Esc
9. Buka Detail Ahmad Dahlan lalu Tab Role (Sub-tab Global Role)
10. Hover switch Global Role dan checkbox C/R/U/D
11. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `Default User cannot be modified.`
12. Buka Sub-tab Group Role
13. Hover `[Assign Group]` pada baris Group Role
14. Verifikasi `[Assign Group]` Disabled dengan tooltip `Default User cannot be modified.`
15. Verifikasi `[Detail]` pada baris Group Role Enabled
16. Buka Sub-tab Transaction Role
17. Hover kontrol Transaction Role
18. Verifikasi kontrol Transaction Role Disabled dengan tooltip `Default User cannot be modified.`
19. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
20. Buka Settings > User dari sidebar

Ulangi langkah 1 sampai 18 untuk Manage global user & role (Update) (Qori Akbar).

### TC-FA-SU-71: Target diri sendiri, seluruh kontrol tulis atas akun sendiri terkunci

21. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
22. Buka Settings > User dari sidebar
23. Ketik Search nama aktor sendiri, tekan Enter
24. Hover sakelar Active baris akun sendiri
25. Verifikasi sakelar Active Disabled dengan tooltip `You can't manage your own account from here.`
26. Hover checkbox baris akun sendiri
27. Verifikasi checkbox baris akun sendiri Disabled dengan tooltip `You can't manage your own account from here.`
28. Verifikasi Table Tools User List tampil
29. Buka row action menu `⋯` baris akun sendiri
30. Verifikasi row action `Edit Home Group` Hidden pada baris akun sendiri
31. Tutup row action menu dengan menekan Esc
32. Buka Detail akun sendiri lalu Tab Role (Sub-tab Global Role)
33. Verifikasi header Detail akun sendiri tampil
34. Hover switch Global Role dan checkbox C/R/U/D
35. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `You can't manage your own account from here.`
36. Buka Sub-tab Group Role
37. Hover `[Assign Group]` pada baris Group Role
38. Verifikasi `[Assign Group]` Disabled dengan tooltip `You can't manage your own account from here.`
39. Verifikasi `[Detail]` pada baris Group Role Enabled
40. Buka Sub-tab Transaction Role
41. Hover kontrol Transaction Role
42. Verifikasi kontrol Transaction Role Disabled dengan tooltip `You can't manage your own account from here.`
43. Verifikasi `Edit Home Group` Hidden pada field Home Group di header Detail akun sendiri
44. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
45. Buka Settings > User dari sidebar

Ulangi langkah 23 sampai 43 untuk Manage global user & role (Update) (Qori Akbar), dengan nama aktor sendiri `Qori Akbar`.

46. Ganti akun: logout lalu login sebagai Group Manager (Oscar Pranata)
47. Buka Settings > User dari sidebar

Ulangi langkah 23 sampai 43 untuk Group Manager (Oscar Pranata), dengan nama aktor sendiri `Oscar Pranata`.

### TC-FA-SU-72: Target Total Control dan Read Only bagi aktor Manage global user & role, terkunci

48. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
49. Buka Settings > User dari sidebar

Untuk setiap target pada tabel "Target tier" di `## Prerequisites` (Lina Marlina, lalu Citra Lestari), jalankan langkah 50 sampai 63.

50. Ketik Search nama target, tekan Enter
51. Hover sakelar Active baris target
52. Verifikasi sakelar Active Disabled dengan tooltip `You don't have permission to edit.`
53. Buka Detail target lalu Tab Role (Sub-tab Global Role)
54. Hover switch Global Role dan checkbox C/R/U/D
55. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `You don't have permission to edit.`
56. Buka Sub-tab Group Role
57. Hover `[Assign Group]` pada baris Group Role
58. Verifikasi `[Assign Group]` Disabled dengan tooltip `You don't have permission to edit.`
59. Verifikasi `[Detail]` pada baris Group Role Enabled
60. Buka Sub-tab Transaction Role
61. Hover kontrol Transaction Role
62. Verifikasi kontrol Transaction Role Disabled dengan tooltip `You don't have permission to edit.`
63. Buka Settings > User dari sidebar
64. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
65. Buka Settings > User dari sidebar
66. Ketik Search `Citra Lestari`, tekan Enter
67. Verifikasi sakelar Active baris Citra Lestari Enabled
68. Buka Detail Citra Lestari lalu Tab Role (Sub-tab Global Role)
69. Verifikasi switch dan checkbox C/R/U/D Global Role Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Kunci target (Default User, diri sendiri, tier) ditulis sebagai satu spec negatif per topik (bagian 3a); ditulis per blok role karena langkah tiap aktor berbeda dan ganti akun menuntut Step eksplisit.
- Spec melewati sekitar 35 langkah (69 langkah nominal, 143 langkah dengan ekspansi). Alasan: seluruh blok satu kelas (fungsional kunci target, hanya membaca), ketiga TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap blok menuntut aktor berbeda dengan ganti akun eksplisit. Langkah yang diulang: langkah 1 sampai 18 untuk Qori Akbar (+18), langkah 23 sampai 43 untuk Qori Akbar dan Oscar Pranata (+42), langkah 50 sampai 63 untuk dua target (+14); parameter ada di `## Prerequisites` dan baris pengulangan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris target pada langkah 1, 23, 50, 66 (R-16); menutup row action menu pada langkah 8 dan 31; membuka Settings > User pada langkah 20, 22, 45, 47, 49, 63, 65.
- Langkah 5, 28 adalah anchor permukaan untuk asersi Hidden langkah 7, 30 (bagian 8b butir 2); langkah 33 adalah klausa c TC-FA-SU-71 ("Detail tetap dapat dibuka").
- Temuan untuk QA:
  - TC-FA-SU-70 Expected c ("Resend tetap tersedia sesuai status") tidak punya langkah observasi dan Ahmad Dahlan berstatus aktif sehingga Resend memang tidak tampil; tidak diasersi. TC-FA-SU-70 tidak menyebut tooltip checkbox baris sehingga hanya state Disabled yang diasersi. Pre-setup #23 tidak menyebut baris Group Role untuk Ahmad Dahlan, sehingga `[Assign Group]` pada baris Group Role (langkah 13 sampai 15) bergantung pada baris yang dimiliki Default User.
  - TC-FA-SU-70 Expected d ("Hasil identik untuk aktor Total Control dan Manage global user & role") dijalankan dengan mengulang langkah 1 sampai 18 untuk Qori Akbar.
  - TC-FA-SU-71 Data Uji menyebut tiga aktor (Total Control, Manage global user & role, Group Manager) sedangkan Expected a juga menyebut "Manage user & role"; Pre-setup #6 (Manage user & role Group) tidak dipakai di Data Uji sehingga tidak diuji. Tooltip sakelar tabel dan kontrol Detail diasumsikan sama `You can't manage your own account from here.`.
  - TC-FA-SU-72 Expected c ("Total Control dan Default User tetap dapat mengubah target tier") bertabrakan dengan TC-FA-SU-71 untuk target Lina Marlina bila login sebagai Total Control (kunci diri sendiri); spec hanya mengasersi target Citra Lestari (langkah 67 sampai 69), dan tidak ada langkah untuk Default User (Ahmad Dahlan).
  - Email akun #4 dan #9 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
