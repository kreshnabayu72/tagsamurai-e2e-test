---
id: TC-AC-ACHA-E2E-008-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Menu dan Elemen Halaman Device Allocation per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-50
  - TC-AC-ACHA-51
  - TC-AC-ACHA-53
  - TC-AC-ACHA-54
  - TC-AC-ACHA-55
  - TC-AC-ACHA-56
  - TC-AC-ACHA-57
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu dan Elemen Halaman Device Allocation per Role

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-50, TC-54 | Total Control Distributor PT Global Distribusi (alias TC_DIST) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| TC-50, TC-55 | Default User Distributor (alias DU_DIST) | #28 | `defaultUserDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_DU_PASSWORD` |
| TC-50, TC-56 | Group Manager Group Jakarta Distributor (alias GM_DIST, Agus Hartono) | #29 | `groupManagerDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_DIST_PASSWORD` |
| TC-50, TC-53, TC-57 | Read Only Distributor (alias RO_DIST) | #34 | `readOnlyDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_RO_DIST_PASSWORD` |
| TC-51 | Role tanpa capability Manage allocation Distributor | #41 | `noCapabilityDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_NOCAP_DIST_PASSWORD` |

- Login akun aktor pertama (TC_DIST) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Seed 30 alokasi (Pre-setup #48); Pre-setup #59: untuk tiap akun TC_DIST, DU_DIST, GM_DIST, dan RO_DIST satu transaksi Waiting for Approval milik sendiri dan satu transaksi Canceled milik sendiri (RO_DIST dibuat sebelum haknya diturunkan menjadi Read Only). Allocation ID transaksi Pre-setup #59 per akun dibaca lewat fixture seed (disediakan tim FE/BE), tidak di-hardcode. Spec tidak membuat data dan tidak menjalankan aksi tulis.
- General Settings Pre-setup #1 tidak diubah. State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var lain pada tabel "Role yang diuji" belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### Role TC_DIST (TC-50, TC-54): Total Control Distributor

1. Verifikasi item menu `Allocation > Device Allocation` Show di sidebar (TC-50 a dan TC-54 a)
2. Klik item menu `Allocation > Device Allocation`
3. Verifikasi halaman List Device Allocation terbuka (TC-50 a)
4. Verifikasi tombol `[+ Allocation]` Show (TC-54 b)
5. Verifikasi tombol `[Download]` Show (TC-54 g)
6. Ketik Search `Allocation ID` transaksi Waiting for Approval milik sendiri (Pre-setup #59), tekan Enter
7. Klik `[⋯]` pada baris hasil
8. Verifikasi aksi `Allocation Log` Show pada transaksi Waiting for Approval
9. Verifikasi aksi `Cancel Allocation` pada transaksi Waiting for Approval milik sendiri Show
10. Verifikasi aksi `Edit` pada transaksi Waiting for Approval milik sendiri Show
11. Tekan Esc untuk menutup menu
12. Ganti isi kotak search dengan `Allocation ID` transaksi Canceled milik sendiri (Pre-setup #59), tekan Enter
13. Klik `[⋯]` pada baris hasil
14. Verifikasi aksi `Allocation Log` Show pada transaksi Canceled
15. Verifikasi aksi `Resubmit` pada transaksi Canceled milik sendiri Show
16. Tekan Esc untuk menutup menu
17. Klik `(←)` pada kotak Search

### Ganti akun ke Default User Distributor

18. Logout dari akun Total Control Distributor
19. Login sebagai Default User Distributor (`defaultUserDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_DU_PASSWORD`)

### Role DU_DIST (TC-50, TC-55): Default User Distributor

20. Verifikasi item menu `Allocation > Device Allocation` Show di sidebar (TC-50 b dan TC-55 a)
21. Klik item menu `Allocation > Device Allocation`
22. Verifikasi halaman List Device Allocation terbuka (TC-50 b)
23. Verifikasi tombol `[+ Allocation]` Show (TC-55 b)
24. Verifikasi tombol `[Download]` Show (TC-55 g)
25. Ketik Search `Allocation ID` transaksi Waiting for Approval milik sendiri (Pre-setup #59), tekan Enter
26. Klik `[⋯]` pada baris hasil
27. Verifikasi aksi `Allocation Log` Show pada transaksi Waiting for Approval
28. Verifikasi aksi `Cancel Allocation` pada transaksi Waiting for Approval milik sendiri Show
29. Verifikasi aksi `Edit` pada transaksi Waiting for Approval milik sendiri Show
30. Tekan Esc untuk menutup menu
31. Ganti isi kotak search dengan `Allocation ID` transaksi Canceled milik sendiri (Pre-setup #59), tekan Enter
32. Klik `[⋯]` pada baris hasil
33. Verifikasi aksi `Allocation Log` Show pada transaksi Canceled
34. Verifikasi aksi `Resubmit` pada transaksi Canceled milik sendiri Show
35. Tekan Esc untuk menutup menu
36. Klik `(←)` pada kotak Search

### Ganti akun ke Group Manager Group Jakarta Distributor

37. Logout dari akun Default User Distributor
38. Login sebagai Group Manager Group Jakarta Distributor (`groupManagerDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_GM_DIST_PASSWORD`)

### Role GM_DIST (TC-50, TC-56): Group Manager Group Jakarta Distributor

39. Verifikasi item menu `Allocation > Device Allocation` Show di sidebar (TC-50 c dan TC-56 a)
40. Klik item menu `Allocation > Device Allocation`
41. Verifikasi halaman List Device Allocation terbuka (TC-50 c)
42. Verifikasi tombol `[+ Allocation]` Show (TC-56 b)
43. Verifikasi tombol `[Download]` Show (TC-56 g)
44. Ketik Search `Allocation ID` transaksi Waiting for Approval milik sendiri (Pre-setup #59), tekan Enter
45. Klik `[⋯]` pada baris hasil
46. Verifikasi aksi `Allocation Log` Show pada transaksi Waiting for Approval
47. Verifikasi aksi `Cancel Allocation` pada transaksi Waiting for Approval milik sendiri Show
48. Verifikasi aksi `Edit` pada transaksi Waiting for Approval milik sendiri Show
49. Tekan Esc untuk menutup menu
50. Ganti isi kotak search dengan `Allocation ID` transaksi Canceled milik sendiri (Pre-setup #59), tekan Enter
51. Klik `[⋯]` pada baris hasil
52. Verifikasi aksi `Allocation Log` Show pada transaksi Canceled
53. Verifikasi aksi `Resubmit` pada transaksi Canceled milik sendiri Show
54. Tekan Esc untuk menutup menu
55. Klik `(←)` pada kotak Search

### Ganti akun ke Read Only Distributor

56. Logout dari akun Group Manager Distributor
57. Login sebagai Read Only Distributor (`readOnlyDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_RO_DIST_PASSWORD`)

### Role RO_DIST (TC-50 d, TC-53, TC-57): Read Only Distributor

58. Verifikasi item menu `Allocation > Device Allocation` Show di sidebar (TC-50 d dan TC-57 a)
59. Klik item menu `Allocation > Device Allocation`
60. Verifikasi halaman List Device Allocation terbuka (TC-50 d)
61. Verifikasi ikon Search, Filter, dan Download Show dan aktif (TC-53 b)
62. Verifikasi tombol `[Download]` Show (TC-57 g)
63. Verifikasi tombol `[+ Allocation]` Hidden (TC-53 a dan TC-57 b)
64. Klik `[⋯]` pada baris pertama tabel
65. Verifikasi menu row action hanya memuat `Allocation Log` (TC-53 c)
66. Tekan Esc untuk menutup menu
67. Ketik Search `Allocation ID` transaksi Waiting for Approval milik sendiri (Pre-setup #59), tekan Enter
68. Klik `[⋯]` pada baris hasil
69. Verifikasi aksi `Allocation Log` Show pada transaksi Waiting for Approval
70. Verifikasi aksi `Cancel Allocation` pada transaksi Waiting for Approval milik sendiri Hidden
71. Verifikasi aksi `Edit` pada transaksi Waiting for Approval milik sendiri Hidden
72. Tekan Esc untuk menutup menu
73. Ganti isi kotak search dengan `Allocation ID` transaksi Canceled milik sendiri (Pre-setup #59), tekan Enter
74. Klik `[⋯]` pada baris hasil
75. Verifikasi aksi `Allocation Log` Show pada transaksi Canceled
76. Verifikasi aksi `Resubmit` pada transaksi Canceled milik sendiri Hidden
77. Tekan Esc untuk menutup menu
78. Klik `(←)` pada kotak Search

### Ganti akun ke role tanpa capability Manage allocation

79. Logout dari akun Read Only Distributor
80. Login sebagai role tanpa capability Manage allocation Distributor (`noCapabilityDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_NOCAP_DIST_PASSWORD`)

### Role tanpa capability (TC-51): menu Hidden

81. Amati sidebar menu Allocation (akun berada di Dashboard Admin Console setelah login)
82. Verifikasi item menu Dashboard tampil di sidebar
83. Verifikasi item `Allocation > Device Allocation` Hidden (tidak dirender sama sekali di sidebar)

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec Role Matrix visibilitas (bagian 3a): satu daftar elemen, banyak role, hasil berbeda per role; polaritas tampil dan Hidden dicampur. Spec hanya membaca; tidak ada aksi tulis.
- Spec ditulis per blok role (bukan perulangan tabel) karena ganti akun menuntut Step eksplisit dan akun pertama login di hook `before` (bagian 3a, `[KEPUTUSAN 2026-10-30]`). Langkah blok TC_DIST, DU_DIST, dan GM_DIST identik kecuali nilai harapan; blok RO_DIST memuat langkah tambahan TC-53.
- Rujukan TC pada langkah: satu `Verifikasi` yang memenuhi Expected dua TC (menu Show pada TC-50 dan TC-54 sampai TC-57; `[+ Allocation]` Hidden pada TC-53 a dan TC-57 b) menyebut kedua id TC di akhir kalimat.
- Langkah penghubung (S-03): langkah klik item menu `Allocation > Device Allocation`, langkah Search untuk menemukan transaksi Pre-setup #59 (Allocation ID dari fixture seed), `Esc` yang menutup menu, `(←)` yang mereset Search, dan langkah ganti akun (logout dan login pada subjudul "Ganti akun ..."). Asersi Hidden pada menu row action didahului `Verifikasi` aksi `Allocation Log` Show pada menu yang sama sebagai anchor.
- Pembagian TC lintas spec: eksekusi aksi per capability positif di spec 010 dan negatif di spec 011; akses ditolak entity gate dan direct URL (TC-48, TC-49, TC-52) di spec 009.
- Ukuran spec (di atas sekitar 35 langkah): empat role dengan langkah baris yang sama dikalikan role (bagian 3a) dan tiap Expected menjadi `Verifikasi` sendiri (S-01). Satu dataset (Pre-setup #59 dan seed), tanpa aksi tulis, dan tiap blok role berdiri sendiri dengan login eksplisit sehingga bagian sesudahnya tetap bermakna bila blok sebelumnya gagal.
- Temuan untuk QA:
  - TC-50 sampai TC-57 menyebut "Tombol `[Download]`" sedangkan Table Tools menampilkan ikon Download (TC-1); spec menganggap keduanya elemen Download pada Table Tools.
  - TC-54 sampai TC-57 mensyaratkan transaksi milik akun sendiri (Pre-setup #59) tanpa Allocation ID; spec membacanya lewat fixture seed.
  - TC-50 Expected d menyatakan "capability Read cukup" sebagai alasan; diasersi hanya sebagai menu Show dan halaman List terbuka.
  - TC-53 (Read Only, "row action hanya `Allocation Log` pada baris mana pun") dan TC-57 (Read Only, matriks tujuh elemen) tumpang tindih pada `[+ Allocation]` Hidden; kedua id disebut pada satu `Verifikasi`.
  - TC-51 Precondition b menyebut akun berada di Dashboard Admin Console; spec memulai dari halaman landing setelah login.
  - Post Condition TC-50 sampai TC-57 bernilai `-`.
