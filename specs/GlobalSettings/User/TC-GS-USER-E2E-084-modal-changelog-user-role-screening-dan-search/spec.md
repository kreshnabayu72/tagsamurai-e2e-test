---
id: TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search
title: "Modal Changelog Role: screening, state kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-510
  - TC-GS-USER-511
  - TC-GS-USER-512
  - TC-GS-USER-513
  - TC-GS-USER-514
  - TC-GS-USER-515
  - TC-GS-USER-516
  - TC-GS-USER-517
  - TC-GS-USER-1053
coverage:
  web: automated
---

# Modal Changelog Role: screening, state kosong, dan Search

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control Siti Nurhaliza (`Siti N`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), akun default suite. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User).
- Pelaku seeding lewat sesi API (tidak login UI): Manage user and role (Full CRUD) Fajar Nugroho (`Fajar N`), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 4), `Spectra.env.GS_FULLCRUD_PASSWORD`. Fajar menjadi nilai Modified By kedua selain `Siti N`.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak dipakai. TC menyebut `Ahmad Fauzi` (Tabel Data Uji Pre-setup baris 13); aksi tulis Role memakai user seed milik spec (S-06), jadi Pre-setup tidak diubah.
- Data Dinamis: user seed `Ahmad Fauzi {runId}-084`, email `ahmadfauzi+{runId}-084@qwertysystem.net`, Access `Global Settings`, bukan tier, field wajib lain diisi seadanya oleh seeding. Judul modal dan nama berkas memakai nama bersuffix ini.
- Seeding minimal (S-11; lewat API di hook `before`, urutan sebagai berikut; setiap role dan aksi setara TC-GS-USER-902, 903, 904, 1052). Entri yang diasersi:
  - 1. Siti N: Assign `Manage TAG` -> baris `Assign | Manage TAG | Access | — | Assigned | Siti N`.
  - 2. Siti N: centang Update `Manage TAG` -> baris `Edit | Manage TAG | Update | Inactive | Active | Siti N`.
  - 3. Fajar N: Assign `Manage files` -> baris `Assign | Manage files | Access | — | Assigned | Fajar N`.
  - 4. Siti N: Remove `Manage files` -> baris `Remove | Manage files | Access | Assigned | — | Siti N`.
  - 5. Siti N: centang Read `Manage hardware` -> baris `Assign | Manage hardware | Access | — | Assigned | Siti N`.
  - 6. Fajar N: centang Update `Manage hardware` -> baris `Edit | Manage hardware | Update | Inactive | Active | Fajar N`.
  - Sebelum entri 1: pemicu Auto-Revert pada user seed (Siti N memberi Access Level lalu menghapusnya lewat edit CRUD di Tab Role, setara TC-GS-USER-381) agar ada entri Auto-Revert di Changelog User yang tidak boleh muncul di Changelog Role (TC-GS-USER-510 butir c). Pemicu persis disediakan tim FE/BE; TC tidak memberi caranya.
  - Nilai distinct (S-11): Action 3 (`Assign`, `Edit`, `Remove`), Role 3, Field 2 (`Access`, `Update`), Old Value 3 (`—`, `Inactive`, `Assigned`), New Value 3 (`Assigned`, `Active`, `—`), Modified By 2 (`Siti N`, `Fajar N`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user seed lewat API; pulihkan visibilitas kolom Modal Changelog Role ke default (7 kolom tampil) lewat penghapusan key `localStorage` tabel itu (nama key disediakan tim FE). Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: menyalin teks sel kolom Date; hover sel Modified By; mengetik kotak Search modal; membaca dan menghapus key `localStorage`.
- Precondition TC-GS-USER-510, 511, 512, 513, 514, 515, 516, 517, 1053: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi (seeding di atas).
- Suite serial (`parallel: false`), lihat `suite.md`.
- State global yang dipulihkan: visibilitas kolom Modal Changelog Role (default).

## Test Steps

### TC-GS-USER-510: Screening Modal Changelog User > Role

1. Ketik Search `Ahmad Fauzi {runId}-084`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-084` di User List
3. Klik Tab `Role`
4. Klik icon Changelog di toolbar Tab Role
5. Verifikasi bagian Header: Title `Changelog: Ahmad Fauzi {runId}-084 > Role`
6. Verifikasi bagian Header: icon `[✕]`
7. Verifikasi bagian Body: toolbar `Search | Filter | Download`
8. Klik icon Search
9. Verifikasi bagian Body: placeholder Search `Search action, role, field, or value...`
10. Klik icon panah `(←)` untuk menutup Search
11. Verifikasi bagian Body: kolom `Date | Action | Role | Field | Old Value | New Value | Modified By | Column Visibility (⋯)`
12. Verifikasi baris Action `Assign` tampil di tabel
13. Verifikasi tidak ada baris Action `Auto-Revert`
14. Verifikasi bagian Footer: pagination

### TC-GS-USER-1053: Hover Modified By menampilkan nama lengkap

15. Hover sel Modified By `Siti N`
16. Verifikasi Tooltip `Siti Nurhaliza`
17. Klik header Modified By
18. Verifikasi Modified By ascending memakai nama lengkap (baris `Fajar N` di atas baris `Siti N`)
19. Klik header Modified By dua kali (Modified By descending, lalu kembali ke default sort tabel)

### TC-GS-USER-511: Siklus Search: reveal, Enter, clear, dan collapse

20. Klik icon Search
21. Verifikasi search bar melebar
22. Verifikasi kursor auto-focus pada input Search
23. Ketik `edit` pada input Search (tanpa Enter)
24. Verifikasi tabel belum tersaring (baris Action `Remove` masih tampil)
25. Verifikasi icon `(✕)` muncul
26. Tekan Enter
27. Verifikasi baris Action `Edit` tampil
28. Verifikasi tabel tersaring (baris Action `Remove` tidak tampil)
29. Klik icon `(✕)`
30. Verifikasi input Search kosong
31. Verifikasi tabel tetap hasil terakhir (baris Action `Remove` tetap tidak tampil)
32. Tekan Enter pada input kosong
33. Verifikasi tabel kembali menampilkan semua data (baris Action `Remove` tampil)
34. Isi Search dengan `edit`, tekan Enter
35. Klik icon panah `(←)`
36. Verifikasi search bar collapse
37. Verifikasi tabel langsung di-reset (baris Action `Remove` tampil)
38. Klik icon Search
39. Verifikasi input Search kosong (keyword tidak tersimpan)

### TC-GS-USER-512: Query Search di-trim dan tidak case-sensitive

40. Isi Search dengan `  ASSIGN  `, tekan Enter
41. Verifikasi baris Action `Assign` tampil
42. Verifikasi isi search box tetap `  ASSIGN  ` apa adanya

### TC-GS-USER-513: Search menemukan substring pada kolom kelas teks

43. Ganti isi kotak search dengan `remov`, tekan Enter
44. Verifikasi Action: baris Action `Remove` tampil
45. Klik icon `(✕)`, lalu tekan Enter pada input kosong
46. Isi Search dengan `hardw`, tekan Enter
47. Verifikasi Role: baris Role `Manage hardware` tampil
48. Klik icon `(✕)`, lalu tekan Enter pada input kosong
49. Isi Search dengan `upda`, tekan Enter
50. Verifikasi Field: baris Field `Update` tampil
51. Klik icon `(✕)`, lalu tekan Enter pada input kosong
52. Isi Search dengan `fajar`, tekan Enter
53. Verifikasi Modified By: baris Modified By `Fajar N` tampil
54. Klik icon `(✕)`, lalu tekan Enter pada input kosong

### TC-GS-USER-514: Search menemukan substring pada kolom kelas nilai campuran

55. Isi Search dengan `inact`, tekan Enter
56. Verifikasi Old Value: baris Old Value `Inactive` tampil
57. Klik icon `(✕)`, lalu tekan Enter pada input kosong
58. Isi Search dengan `assigne`, tekan Enter
59. Verifikasi New Value: baris New Value `Assigned` tampil
60. Klik icon `(✕)`, lalu tekan Enter pada input kosong

### TC-GS-USER-515: Kolom non-searchable tidak tercakup Search

61. Verifikasi baris Action `Assign` tampil (pembanding sebelum Search tanggal)
62. Salin teks tanggal pada kolom Date salah satu baris yang tampil (format yang tampil di kolom itu)
63. Isi Search dengan teks tanggal yang disalin, tekan Enter
64. Verifikasi no result state (`No results found`)

### TC-GS-USER-517: Empty filtered state

65. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
66. Verifikasi empty filtered state tampil: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
67. Klik icon `(✕)`, lalu tekan Enter pada input kosong

### TC-GS-USER-516: Search tidak mencocokkan kolom yang di-hide, kembali cocok setelah unhide

68. Isi Search dengan `fajar`, tekan Enter
69. Verifikasi baris Modified By `Fajar N` tampil (pembanding sebelum kolom di-hide)
70. Klik header kolom Column Visibility (⋯), hilangkan centang `Modified By` pada overlay, lalu tutup overlay
71. Tekan Enter pada input Search
72. Verifikasi no result state (`No results found`)
73. Klik header kolom Column Visibility (⋯), centang kembali `Modified By` pada overlay, lalu tutup overlay
74. Tekan Enter pada input Search
75. Verifikasi baris Modified By `Fajar N` tampil kembali

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka sekali di langkah 2 sampai 4 untuk semua TC.
- Urutan TC dalam spec: TC-GS-USER-510, 1053, 511, 512, 513, 514, 515, 517, 516. Alasan: screening (510) dan hover (1053) tanpa aksi Search di awal (bagian 3 konvensi); TC-GS-USER-516 di akhir karena mengubah visibilitas kolom (preferensi di `localStorage`) dan memulihkannya di langkah 73; TC-GS-USER-515 sebelum TC-GS-USER-517 hanya karena keduanya memakai satu kotak Search yang sudah terbuka.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama baris persis sebelum Klik Name, karena User List bisa lebih dari satu halaman; akhiran runId saja tidak cukup), langkah 10 (menutup Search sesudah asersi placeholder), 19 (mengembalikan sort Modified By ke default), 43, 46, 49, 52, 55, 58, dan 67 (mengosongkan kotak search dan mereset tabel, memenuhi "lalu clear" di TC), serta langkah 70, 73 (membuka dan menutup overlay Column Visibility; hide dan unhide adalah aksi TC).
- Langkah baru di TC-GS-USER-511 (S-03): membuka kembali Search sesudah `(←)` (langkah 38) adalah langkah penghubung untuk mengamati "keyword kosong" (Expected f), dan `Verifikasi input Search kosong` (langkah 39) adalah klausa itu; langkah 40 mengisi kotak yang sudah terbuka.
- Langkah 12, 24, 28, 31, 33, 37, 61, dan 69 adalah anchor positif untuk asersi ketiadaan (baris `Remove` tidak tampil, no result state; S-03, bagian 8b butir 2). Pada TC-GS-USER-516 anchor (langkah 68 dan 69) ditaruh sebelum kolom di-hide; urutan TC (hide dulu, lalu Search) diubah supaya hasil kosong bukan karena salah ketik. Expected a dan b TC tetap terpenuhi (langkah 72 dan 75).
- Asersi memakai pola baris (bukan jumlah baris). Keyword substring dipilih agar tiap kolom punya nilai yang dikenali: `remov` (Action), `hardw` (Role), `upda` (Field), `fajar` (Modified By), `inact` (Old Value), `assigne` (New Value). Keyword `assigne` juga cocok dengan Old Value baris `Remove`; Expected TC hanya menuntut baris New Value `Assigned` tampil.
- Spec melewati sekitar 35 langkah (75 langkah) karena tiap kolom searchable pada TC-GS-USER-513 dan 514 memerlukan aksi Search, `Verifikasi`, dan pembersihan sendiri, dan tiap klausa Expected TC-GS-USER-510 dan 511 menjadi satu `Verifikasi` (S-01). Semua blok satu kelas harness (screening dan Search satu Modal Changelog Role), satu akun, satu dataset, dan tiap blok berdiri sendiri karena kotak search dikosongkan dan tabel direset di akhir blok; modal dibuka sekali.
- TC terbagi lintas spec: TC-GS-USER-516 hanya mengasersi Search pada kolom hidden di spec ini; filter pada kolom hidden (TC-GS-USER-530) diverifikasi di spec 086, dan Download tanpa kolom hidden (TC-GS-USER-547) di spec 089.
- Temuan untuk QA: (1) TC-GS-USER-510 butir c ("tidak menampilkan baris Auto-Revert") tidak memberi cara membangkitkan entri Auto-Revert; spec memakai pemicu setara TC-GS-USER-381 yang disediakan tim FE/BE. (2) TC-GS-USER-1053 Expected "sort Modified By memakai nama lengkap" tidak dapat dibedakan dari sort nama singkat dengan akun `Fajar N` dan `Siti N` (urutan sama pada nama lengkap maupun singkat); spec hanya mengasersi urutan baris. (3) TC-GS-USER-510, 511, dan lainnya menyebut `Ahmad Fauzi` dan nama berkas tanpa suffix; spec memakai user seed bersuffix sehingga judul modal berbeda dari teks TC. (4) TC-GS-USER-511 Expected b dan d tidak menyebut cara mengamati "tabel belum tersaring"; spec memakai ada atau tidaknya baris Action `Remove` sebagai penanda. (5) TC-GS-USER-515 Data Uji menyebut "nilai tanggal/status", tetapi tabel tidak punya kolom status; spec memakai nilai kolom Date. (6) TC-GS-USER-513 dan 514 "lalu clear" tidak menyebut cara; spec memakai `(✕)` lalu Enter pada input kosong. (8) TC-GS-USER-511 Expected f "keyword kosong" tidak menyebut cara mengamati; spec membuka kembali Search dan memeriksa input kosong. (7) Format nama singkat `Fajar N` untuk Fajar Nugroho mengikuti pola `Siti N` di TC; TC tidak menyebutnya eksplisit.
