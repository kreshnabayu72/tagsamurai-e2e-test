---
id: TC-FA-COA-E2E-003-accessibility-switch-status-fokus-modal-dan-atribut-aria-form
title: "Accessibility: Switch Status, Fokus Modal, dan Atribut ARIA Form"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-161
  - TC-FA-COA-162
  - TC-FA-COA-291
  - TC-FA-COA-292
coverage:
  web: automated
---

# Accessibility: Switch Status, Fokus Modal, dan Atribut ARIA Form

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001 – Depreciation Expense – Admin` (Active, Used By 0, belum pernah diekspor) dan P7 `4-7002 – Gain and Loss on Disposal` (Active, Used By 2: Asset Class `Delivery Vehicles` dan `Heavy Equipment`). Form Edit P1 hanya dibuka dan `[Save]` ditolak validasi (field dikosongkan), sehingga P1 dan Last Updated-nya tidak berubah (S-06).
- Kemampuan teknis: keyboard (Tab, Space, Esc); pembacaan atribut DOM `aria-label`, `aria-required`, dan `aria-describedby` dari elemen yang diperiksa.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-161: Accessibility Switch Status: label aksesibilitas, state checked, dan aktivasi lewat keyboard

1. Ketik Search `5-6001`, tekan Enter
2. Tekan Tab sampai fokus berada di Switch Status baris P1
3. Verifikasi Switch Status baris P1 menerima fokus keyboard
4. Verifikasi label aksesibilitas Switch Status baris P1 `Status for account 5-6001`
5. Verifikasi Switch Status baris P1 berstate checked
6. Tekan Space
7. Verifikasi dialog `Deactivate Account` (D-01) tampil dengan bullet `• 5-6001 – Depreciation Expense – Admin`
8. Tekan Tab beberapa kali selama dialog terbuka
9. Verifikasi fokus ter-trap di dalam dialog D-01: Tab berulang berputar di antara `[Cancel]` dan `[Deactivate]` dan tidak keluar ke tabel
10. Klik `[Cancel]` pada dialog
11. Verifikasi Switch Status baris P1 tetap Active
12. Klik `(←)` pada kotak Search

### TC-FA-COA-162: Accessibility keyboard: fokus ter-trap di modal Add Account, Esc menutup modal dan popup Used By

13. Ketik Search `4-7002`, tekan Enter
14. Klik `+ Account`
15. Tekan Tab berulang sebanyak elemen interaktif di modal sampai kembali ke elemen pertama
16. Verifikasi fokus berputar di dalam modal Add Account dan tidak berpindah ke elemen di luar modal (tabel di belakang modal)
17. Tekan Esc
18. Verifikasi modal Add Account tertutup
19. Verifikasi baris P7 `4-7002` tampil di tabel
20. Verifikasi dialog `Unsaved Changes` tidak tampil
21. Klik angka `2` di kolom Used By baris P7
22. Verifikasi popup `Used By` terbuka
23. Tekan Esc
24. Verifikasi popup `Used By` tertutup
25. Klik `(←)` pada kotak Search

### TC-FA-COA-291: Accessibility form Add Account: `aria-required` pada field wajib dan `aria-describedby` pada field dengan caption error

26. Klik `+ Account` di toolbar
27. Verifikasi `aria-required` bernilai true pada Account Code
28. Verifikasi `aria-required` bernilai true pada Account Name
29. Verifikasi `aria-required` bernilai true pada Account Function
30. Klik `[Submit]` dengan field kosong
31. Verifikasi Account Code memiliki `aria-describedby` yang menunjuk caption error Account Code
32. Verifikasi Account Name memiliki `aria-describedby` yang menunjuk caption error Account Name
33. Verifikasi Account Function memiliki `aria-describedby` yang menunjuk caption error Account Function
34. Klik `✕` di header modal Add Account

### TC-FA-COA-292: Accessibility form Edit Account: `aria-required` pada field wajib dan `aria-describedby` pada field dengan caption error

35. Ketik Search `5-6001`, tekan Enter
36. Klik row action `Edit` pada baris P1
37. Verifikasi `aria-required` bernilai true pada Account Code
38. Verifikasi `aria-required` bernilai true pada Account Name
39. Verifikasi `aria-required` bernilai true pada Account Function
40. Klik `[Clear Field]`
41. Klik `[Save]`
42. Verifikasi Account Code memiliki `aria-describedby` yang menunjuk caption error Account Code
43. Verifikasi Account Name memiliki `aria-describedby` yang menunjuk caption error Account Name
44. Verifikasi Account Function memiliki `aria-describedby` yang menunjuk caption error Account Function
45. Klik `✕` di header modal Edit Account
46. Verifikasi dialog `Unsaved Changes` tampil
47. Klik `[Leave]`
48. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 1, 13, 35 (Search untuk menemukan baris P1 atau P7 sebelum aksi pada baris itu; bagian 8b butir 13, R-16); langkah 12, 25, 48 (menutup Search dan mereset tabel, S-09); langkah 34 (menutup modal Add Account setelah `[Submit]` ditolak validasi; form tidak diisi sehingga tidak dirty dan dialog `Unsaved Changes` tidak diharapkan, tidak ada kasus bersyarat); langkah 45 sampai 47 (S-08: form Edit dirty setelah `[Clear Field]` ditutup lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, `[Leave]`).
- Asersi tambahan di luar Expected TC (S-03): langkah 19 menjadi anchor positif untuk langkah 20 (absence dialog `Unsaved Changes`, bagian 8b butir 2).
- Atribut ARIA diperiksa per field (S-01): `aria-required` pada Account Code, Account Name, dan Account Function (langkah 27 sampai 29 dan 37 sampai 39); `aria-describedby` pada tiap field yang menampilkan caption error (langkah 31 sampai 33 dan 42 sampai 44). Kosongnya ketiga field setelah `[Submit]` atau `[Clear Field]` lalu `[Save]` diasumsikan menampilkan caption error pada ketiganya.
- Ukuran spec 48 langkah, melewati sekitar 35 langkah karena Expected dipecah per klausa (S-01), terutama atribut ARIA per field. Seluruh blok satu topik (aksesibilitas keyboard dan ARIA halaman Chart of Accounts), satu dataset (P1 dan P7), tanpa aksi tulis ke data, dan tiap blok berdiri sendiri (form dan dialog ditutup di akhir blok); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-COA-161 Post Condition "Status P1 tetap Active; tidak ada log" tidak punya langkah observasi untuk "tidak ada log"; hanya status Active yang diasersi (langkah 11).
  - TC-FA-COA-162 butir c tidak menyebut baris yang terlihat saat mengetuk angka Used By; spec mencari P7 lewat Search sebelum aksi (R-16).
  - TC-FA-COA-291 dan TC-FA-COA-292 tidak menyebut field mana yang memunculkan caption error; spec mengasumsikan ketiganya.
