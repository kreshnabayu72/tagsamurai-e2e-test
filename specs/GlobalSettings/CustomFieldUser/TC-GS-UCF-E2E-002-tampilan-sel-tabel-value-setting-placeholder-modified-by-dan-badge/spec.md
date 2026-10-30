---
id: TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge
title: "Tampilan Sel Tabel Custom Field: Value Setting, Placeholder Efektif, Modified By, Active, Required, Data Type, dan Batas Teks Panjang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-12
  - TC-GS-UCF-13
  - TC-GS-UCF-440
  - TC-GS-UCF-441
  - TC-GS-UCF-14
  - TC-GS-UCF-15
  - TC-GS-UCF-16
  - TC-GS-UCF-17
  - TC-GS-UCF-18
  - TC-GS-UCF-19
  - TC-GS-UCF-20
  - TC-GS-UCF-21
  - TC-GS-UCF-326
  - TC-GS-UCF-371
  - TC-GS-UCF-503
  - TC-GS-UCF-511
  - TC-GS-UCF-512
coverage:
  web: automated
---

# Tampilan Sel Tabel Custom Field: Value Setting, Placeholder Efektif, Modified By, Active, Required, Data Type, dan Batas Teks Panjang

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field; spec ini tidak menguji navigasi sehingga tidak mengulang langkah buka.
- Data Pre-setup Client A (6 field, tetap di environment, hanya dibaca, tanpa suffix): `Cost Center` (Dropdown: Finance, Operations, Marketing; Placeholder `Select cost center`; Required Yes; Modified By `Budi S`), `Employee Grade` (Text; Modified By `Siti R`), `Job Description` (Text Area), `Bonus` (Numeric, Decimal Places 2), `Office Phone` (Phone), `Joining Date` (Date; Inactive).
- Population D-01 (8 field: `Blood Type` Dropdown A, B, AB, O; `Shirt Size` Dropdown dengan Placeholder `Choose shirt size`; `Emergency Phone` Phone; `Birth Date` Date; `Tax ID` Text dengan Placeholder `Enter tax ID number`, Required Yes; `Work Notes` Text Area; `Annual Target` Numeric Decimal Places 1; `badge number` Text): di-seed lewat API di hook `before` (idempotent, dilewati bila sudah ada), nama literal tanpa suffix karena asersi nama tiap baris (pengecualian S-12 butir (i)); fixture baru `Fixture.customFieldUser.population`. Hook `after` hanya menghapus field Population yang dibuat hook `before` spec ini.
- Data Dinamis (di-seed lewat API di hook `before`, milik spec ini, bersuffix `{runId}-002`; fixture baru `Fixture.customFieldUser.display002`):
  - D-02: `Work Shift {runId}-002` (Dropdown: Day, Night; tanpa Placeholder).
  - D-178: `Single Value DD {runId}-002` (Dropdown: Solo; Active).
  - D-179: `Inactive DD {runId}-002` (Dropdown: Sun, Moon; Inactive).
  - D-03: `Long Placeholder Field {runId}-002` (Text; Placeholder 120 karakter `A` diselingi spasi).
  - D-105: field Text dengan Field Name 120 karakter yang diawali `A` berulang dan diakhiri ` {runId}-002` sehingga panjang total termasuk suffix tepat 120 karakter.
  - D-162: `Long Value DD {runId}-002` (Dropdown: `ABCDEFGHIJKLMNOPQRSTUVWXYZ` 26 karakter, `Beta`, `Gamma`).
  - D-232: `Boundary DD {runId}-002` (Dropdown: `ABCDEFGHIJKLMNOPQRSTUVWXY` 25 karakter, `Beta`, `Gamma`).
  - D-233: `Wrap DD {runId}-002` (Dropdown: `ABCDEFGHIJ` diulang 12 kali = 120 karakter, `Beta`, `Gamma`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua field Data Dinamis bersuffix `{runId}-002` yang masih ada; kembalikan ukuran halaman tabel ke 10 bila masih berubah; kosongkan Search tabel.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover; pembacaan teks badge, chip, dan sel tabel; pembacaan panjang karakter sel; pembacaan keberadaan avatar atau badge pada sel; pembacaan tooltip.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan ukuran halaman tabel (dipulihkan langkah 88). Suite berjalan serial (`parallel: false`).

Nilai sel yang diuji (dipakai langkah yang diulang per baris tabel):

| Tabel | Field | Nilai yang diharapkan |
|---|---|---|
| Value Setting `—` (TC-GS-UCF-14) | `Employee Grade` (Text), `Job Description` (Text Area), `Joining Date` (Date), `Office Phone` (Phone) | `—` |
| Placeholder default (TC-GS-UCF-16) | `Employee Grade` / `Blood Type` / `Birth Date` / `Work Notes` / `Annual Target` / `Emergency Phone` | `Enter employee grade` / `Select blood type` / `Select date` / `Enter work notes` / `Enter annual target` / `Enter phone number` |
| Placeholder custom (TC-GS-UCF-17) | `Tax ID` / `Shirt Size` / `Cost Center` | `Enter tax ID number` / `Choose shirt size` / `Select cost center` |
| Required (TC-GS-UCF-20) | `Cost Center` / `Tax ID` / `Employee Grade` | `Yes` / `Yes` / `No` |
| Data Type (TC-GS-UCF-503) | `Cost Center` / `Employee Grade` / `Job Description` / `Bonus` / `Office Phone` / `Joining Date` | `Dropdown` / `Text` / `Text Area` / `Numeric` / `Phone` / `Date` |

## Test Steps

1. Ubah ukuran halaman tabel menjadi 100 supaya seluruh baris Pre-setup, Population, dan Data Dinamis spec ini tampil di halaman 1

### TC-GS-UCF-12: Value Setting Dropdown lebih dari dua value menampilkan dua badge lalu chip `+N more`

2. Amati sel Value Setting baris `Cost Center` dan baris `Blood Type`
3. Verifikasi baris `Cost Center`: badge `Finance`, badge `Operations`, lalu chip `+1 more`
4. Verifikasi baris `Blood Type`: badge `A`, badge `B`, lalu chip `+2 more`
5. Verifikasi urutan badge pada kedua baris mengikuti urutan penambahan value (value baru di akhir)

### TC-GS-UCF-13: Value Setting Dropdown dengan dua value atau kurang tanpa chip `+N more`

6. Ketik Search `work shift`, tekan Enter
7. Verifikasi sel Value Setting baris `Work Shift {runId}-002` menampilkan badge `Day` dan badge `Night`
8. Verifikasi sel Value Setting baris `Work Shift {runId}-002` tidak memiliki chip `+N more`
9. Klik `(←)` pada kotak Search

### TC-GS-UCF-440: Value Setting Dropdown dengan satu value

10. Ketik Search `Single Value DD`, tekan Enter
11. Verifikasi sel Value Setting baris `Single Value DD {runId}-002` menampilkan satu badge `Solo`
12. Verifikasi sel Value Setting baris `Single Value DD {runId}-002` tidak memiliki chip `+N more`
13. Klik `(←)` pada kotak Search

### TC-GS-UCF-441: Value Setting field Dropdown yang Inactive tetap tampil di List

14. Ketik Search `Inactive DD`, tekan Enter
15. Verifikasi switch Active baris `Inactive DD {runId}-002` Off
16. Verifikasi sel Value Setting baris `Inactive DD {runId}-002` menampilkan badge `Sun` dan badge `Moon`
17. Klik `(←)` pada kotak Search

### TC-GS-UCF-14: Value Setting Numeric menampilkan Decimal Places dan tipe lain menampilkan strip

18. Amati sel Value Setting baris `Bonus` dan baris `Annual Target`
19. Verifikasi sel Value Setting baris `Bonus` menampilkan `2 Decimal Places`
20. Verifikasi sel Value Setting baris `Annual Target` menampilkan `1 Decimal Place`
21. Untuk setiap baris pada tabel "Value Setting `—`" (langkah 21): Verifikasi sel Value Setting baris tersebut menampilkan `—` (bukan kosong)

### TC-GS-UCF-15: Klik chip `+N more` membuka popup All Values Preview read-only

22. Klik chip `+1 more` pada baris `Cost Center`
23. Verifikasi popup terbuka dengan judul `All Values` dan baris identitas `Cost Center (3)` di bawah judul
24. Verifikasi seluruh value `Finance`, `Operations`, dan `Marketing` tampil sebagai badge
25. Verifikasi popup tidak memiliki aksi selain icon close
26. Verifikasi popup tidak memiliki tombol teks `Close`
27. Klik backdrop di luar popup
28. Verifikasi popup tetap terbuka (klik backdrop tidak menutup popup)
29. Klik icon close pada popup
30. Verifikasi popup tertutup

### TC-GS-UCF-16: Kolom Placeholder menampilkan nilai efektif (default per Data Type bila Placeholder kosong)

31. Untuk setiap baris pada tabel "Placeholder default" (langkah 31): Verifikasi sel Placeholder baris tersebut menampilkan nilai default pada tabel

### TC-GS-UCF-17: Kolom Placeholder menampilkan Placeholder yang diisi dan tidak membedakan custom dari default

32. Untuk setiap baris pada tabel "Placeholder custom" (langkah 32): Verifikasi sel Placeholder baris tersebut menampilkan nilai pada tabel
33. Verifikasi tidak ada penanda visual yang membedakan sel Placeholder custom (`Tax ID`, `Shirt Size`, `Cost Center`) dari sel Placeholder default (`Employee Grade`)

### TC-GS-UCF-18: Modified By tampil format singkat plain text dan hover menampilkan nama lengkap

34. Amati kolom Modified By baris `Cost Center` dan baris `Employee Grade`
35. Verifikasi sel Modified By baris `Cost Center` menampilkan `Budi S` sebagai plain text
36. Verifikasi sel Modified By baris `Cost Center` tanpa avatar
37. Verifikasi sel Modified By baris `Cost Center` tanpa badge
38. Verifikasi sel Modified By baris `Employee Grade` menampilkan `Siti R` sebagai plain text
39. Verifikasi sel Modified By baris `Employee Grade` tanpa avatar
40. Verifikasi sel Modified By baris `Employee Grade` tanpa badge
41. Arahkan kursor ke `Budi S` pada baris `Cost Center`
42. Verifikasi tooltip `Budi Santoso`
43. Arahkan kursor ke `Siti R` pada baris `Employee Grade`
44. Verifikasi tooltip `Siti Rahmawati`

### TC-GS-UCF-19: Kolom Active menampilkan switch On untuk field Active dan Off untuk field Inactive

45. Amati kolom Active baris `Cost Center` dan baris `Joining Date`
46. Verifikasi switch Active baris `Cost Center` On
47. Verifikasi switch Active baris `Joining Date` Off
48. Verifikasi kolom Active berada di posisi pertama setelah kolom Checkbox

### TC-GS-UCF-20: Kolom Required menampilkan badge Yes atau No

49. Untuk setiap baris pada tabel "Required" (langkah 49): Verifikasi sel Required baris tersebut menampilkan badge dengan nilai pada tabel

### TC-GS-UCF-21: Placeholder 120 karakter di sel tabel tampil penuh tanpa tooltip

50. Ketik Search `Long Placeholder Field`, tekan Enter
51. Amati sel Placeholder baris `Long Placeholder Field {runId}-002`
52. Verifikasi teks Placeholder tampil penuh (120 karakter, wrap natural) tanpa pemotongan `..`
53. Arahkan kursor ke sel Placeholder
54. Verifikasi hover tidak menampilkan tooltip
55. Verifikasi tinggi baris menyesuaikan tanpa merusak kolom lain
56. Klik `(←)` pada kotak Search

### TC-GS-UCF-326: Field Name 120 karakter tampil utuh di sel tabel tanpa dipotong

57. Ketik Search `AAAAAAAAAA`, tekan Enter
58. Amati sel Field Name baris tersebut
59. Verifikasi Field Name tampil utuh (120 karakter) tanpa pemotongan `..`
60. Arahkan kursor ke sel Field Name
61. Verifikasi hover tidak menampilkan tooltip
62. Verifikasi kolom Field Name melebar tanpa merusak kolom lain
63. Klik `(←)` pada kotak Search

### TC-GS-UCF-371: Badge value Dropdown panjang dipotong di List dan tampil penuh di popup All Values

64. Ketik Search `Long Value DD`, tekan Enter
65. Verifikasi kolom Value Setting menampilkan badge `ABCDEFGHIJKL..OPQRSTUVWXYZ`
66. Verifikasi kolom Value Setting menampilkan badge `Beta`
67. Verifikasi kolom Value Setting menampilkan chip `+1 more`
68. Arahkan kursor ke badge pertama pada kolom Value Setting
69. Verifikasi hover badge pertama menampilkan nilai penuh `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
70. Klik chip `+1 more`
71. Verifikasi popup All Values menampilkan badge penuh `ABCDEFGHIJKLMNOPQRSTUVWXYZ`, `Beta`, dan `Gamma`
72. Klik icon close pada popup
73. Klik `(←)` pada kotak Search

### TC-GS-UCF-503: Kolom Data Type menampilkan label tipe sebagai badge

74. Untuk setiap baris pada tabel "Data Type" (langkah 74): Verifikasi sel Data Type baris tersebut menampilkan badge dengan nilai pada tabel

### TC-GS-UCF-511: Value Dropdown tepat 25 karakter tampil utuh tanpa pemotongan

75. Ketik Search `Boundary DD`, tekan Enter
76. Verifikasi badge pertama menampilkan `ABCDEFGHIJKLMNOPQRSTUVWXY` utuh tanpa `..`
77. Verifikasi badge kedua `Beta`
78. Verifikasi chip `+1 more` tampil
79. Klik `(←)` pada kotak Search

### TC-GS-UCF-512: Popup All Values menampilkan value Dropdown 120 karakter secara penuh

80. Ketik Search `Wrap DD`, tekan Enter
81. Klik chip `+1 more` pada sel Value Setting
82. Verifikasi popup berjudul `All Values` dengan baris identitas `Wrap DD {runId}-002 (3)`
83. Verifikasi badge pertama menampilkan seluruh 120 karakter (`ABCDEFGHIJ` sebanyak 12 kali) tanpa pemotongan `..`
84. Verifikasi badge `Beta` dan `Gamma` tampil
85. Verifikasi popup tidak memiliki aksi selain icon close
86. Klik icon close pada popup
87. Klik `(←)` pada kotak Search
88. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Seluruh asersi adalah tampilan sel tabel (baca).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec mengikuti daftar sumber (12, 13, 440, 441, 14, 15, 16, 17, 18, 19, 20, 21, 326, 371, 503, 511, 512). Tidak ada aksi yang menghapus data; seluruh Data Dinamis dihapus di hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 88 (ukuran halaman 100 supaya baris Pre-setup, Population, dan Data Dinamis ada di halaman aktif dan pemulihannya), langkah 6, 10, 14, 50, 57, 64, 75, dan 80 (Search untuk menemukan baris target; TC-GS-UCF-12, 14, 15, 16, 17, 18, 19, 20, dan 503 tidak memuat Search karena barisnya Pre-setup atau Population), langkah 9, 13, 17, 56, 63, 73, 79, dan 87 (`(←)` menutup input dan mereset tabel), serta langkah 72 dan 86 (menutup popup All Values).
- Langkah yang diulang per baris tabel (langkah 21, 31, 32, 49, 74): parameter tiap iterasi ada di tabel "Nilai sel yang diuji" pada Prerequisites; satu `Verifikasi` per baris (S-01).
- Langkah 33 membandingkan sel custom dengan sel default `Employee Grade` sebagai padanan "tidak membedakan custom dari default" (Expected d TC-GS-UCF-17); TC tidak menyebut cara pembandingnya.
- Spec melewati sekitar 35 langkah (88 langkah nominal). Seluruhnya satu kelas (tampilan sel tabel baca, satu akun, satu dataset); tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: popup All Values pada TC-GS-UCF-15, 371, dan 512 hanya diamati tampilannya; pemakaian field Dropdown di form User ada di spec lain.
- Temuan untuk QA:
  - TC-GS-UCF-14 Expected a dan b memakai `2 Decimal Places` dan `1 Decimal Place` (keputusan NC-10, pluralisasi alami); LLD `/list` masih menulis `<N> decimal place(s)` (dilacak di `nc-followups.md`). Asersi mengikuti TC dan bisa gagal pada backend nyata sampai LLD diselaraskan.
  - TC-GS-UCF-326 menyebut Search `AAAAAAAAAA` dan Field Name 120 karakter `A`; spec memberi suffix ` {runId}-002` sehingga hanya 120 minus panjang suffix karakter pertama berupa `A`, dan panjang total tetap 120 karakter.
  - TC-GS-UCF-21 tidak menyebut pola persis "120 karakter `A` diselingi spasi" (jumlah `A` dan posisi spasi); spec mengasersi teks utuh 120 karakter sama dengan nilai seed.
  - TC-GS-UCF-18 memakai Modified By Pre-setup `Budi S` dan `Siti R`; nilai itu tetap hanya selama tidak ada spec lain yang mengubah `Cost Center` atau `Employee Grade` (S-06).
  - TC-GS-UCF-12 sampai 20 tidak menyebut halaman tempat tiap baris berada; spec memakai ukuran halaman 100 (langkah 1).
  - TC-GS-UCF-13, 441, dan 440 menulis nama field tanpa suffix; spec memakai nama bersuffix dan Search memakai kata kunci tanpa suffix (kata kunci tetap cocok).
  - TC-GS-UCF-15 d menyebut "Klik backdrop tidak menutup popup" tanpa menyebut state popup setelah klik; spec mengasersi popup tetap terbuka (langkah 28).
