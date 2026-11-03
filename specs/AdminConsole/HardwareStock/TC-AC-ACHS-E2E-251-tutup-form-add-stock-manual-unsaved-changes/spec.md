---
id: TC-AC-ACHS-E2E-251-tutup-form-add-stock-manual-unsaved-changes
title: "Tutup Form Add Stock Manual dan Dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-103
  - TC-AC-ACHS-104
  - TC-AC-ACHS-105
  - TC-AC-ACHS-106
  - TC-AC-ACHS-107
coverage:
  web: automated
---

# Tutup Form Add Stock Manual dan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |

- Data Pre-setup: SKU `{skuFx}` (Pre-setup #16, #27).
- Data Dinamis: hanya satu unit yang disimpan, `SN-F5-0001-{runId}-251` (langkah 54), dihapus hook `after`. Serial Number lain (`SN-BC-0001`, `SN-LV-0001`, `SN-NAV-0001`) diketik tetapi selalu dibuang lewat `[Leave]` sehingga literal seperti di TC.
- Kemampuan teknis (disediakan tim FE): mendeteksi, menerima, dan membatalkan dialog `beforeunload` bawaan browser saat F5 (langkah 49, 52, 53, 58); fixture BE yang menghapus unit bersuffix `-{runId}-251` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA).
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU {skuFx} berubah oleh satu unit baru (langkah 54); dihapus hook `after`. Baseline dicatat pada langkah 2.

## Test Steps

### TC-AC-ACHS-103: Cancel pada form manual kosong

1. Ketik Search `{skuFx}`, tekan Enter
2. Catat Total Registered dan Available baris SKU `{skuFx}` sebagai baseline
3. Klik `(⋯)` pada baris SKU `{skuFx}`
4. Klik opsi `Add Stock`
5. Biarkan textarea kosong
6. Klik `[Cancel]`
7. Verifikasi halaman langsung berpindah ke Stock Detail > Tab Available SKU `{skuFx}`
8. Verifikasi dialog Unsaved Changes tidak tampil

### TC-AC-ACHS-105: Breadcrumb pada form manual berisi

9. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
10. Klik segmen `Hardware` pada breadcrumb
11. Verifikasi tidak ada perubahan halaman (segmen pertama tidak bisa diklik)
12. Klik segmen `Add Stock` pada breadcrumb
13. Verifikasi tidak ada perubahan halaman (segmen terakhir tidak bisa diklik)
14. Ketik `SN-BC-0001`
15. Klik segmen `Stock` pada breadcrumb
16. Verifikasi dialog Unsaved Changes tampil
17. Klik `[Leave]`
18. Verifikasi Stock List terbuka (Breadcrumb `Hardware > Stock`)

### TC-AC-ACHS-104: Cancel pada form manual berisi

19. Ketik Search `{skuFx}`, tekan Enter
20. Klik `(⋯)` pada baris SKU `{skuFx}`
21. Klik opsi `Add Stock`
22. Verifikasi textarea kosong (input `SN-BC-0001` dari form sebelumnya dibuang)
23. Ketik `SN-LV-0001`
24. Klik `[Cancel]`
25. Verifikasi dialog Unsaved Changes tampil dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
26. Klik `[Cancel]` pada dialog
27. Verifikasi dialog tertutup dan form tetap terbuka dengan textarea berisi `SN-LV-0001`
28. Klik `[Cancel]` halaman lagi
29. Verifikasi dialog Unsaved Changes tampil
30. Klik `[Leave]` pada dialog
31. Verifikasi halaman berpindah ke Stock Detail > Tab Available tanpa unit baru
32. Verifikasi Summary bar Total Registered dan Available sama dengan baseline langkah 2

### TC-AC-ACHS-106: Link sidebar pada form manual berisi

33. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
34. Ketik `SN-NAV-0001`
35. Klik menu `Approvals` pada sidebar
36. Verifikasi dialog Unsaved Changes tampil
37. Klik `[Cancel]` pada dialog
38. Verifikasi dialog tertutup dan navigasi dibatalkan: form tetap terbuka dengan textarea berisi `SN-NAV-0001`
39. Klik menu `Approvals` pada sidebar lagi
40. Verifikasi dialog Unsaved Changes tampil
41. Klik `[Leave]` pada dialog
42. Verifikasi navigasi dilanjutkan: halaman Approvals terbuka

### TC-AC-ACHS-107: Refresh F5 pada form manual

43. Klik menu Hardware > Stock pada sidebar
44. Ketik Search `{skuFx}`, tekan Enter
45. Klik `(⋯)` pada baris SKU `{skuFx}`
46. Klik opsi `Add Stock`
47. Verifikasi textarea kosong (input `SN-NAV-0001` dari form sebelumnya dibuang)
48. Tekan F5
49. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser: form Add Stock tampil kembali dengan textarea kosong
50. Ketik `SN-F5-0001-{runId}-251`
51. Tekan F5
52. Verifikasi muncul konfirmasi bawaan browser (beforeunload)
53. Batalkan reload (tetap di halaman Add Stock)
54. Klik `[Submit]`
55. Verifikasi toast sukses "Success, unit has been added to stock."
56. Verifikasi halaman berpindah ke Stock Detail > Tab Available
57. Tekan F5
58. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser (guard dilepas setelah Submit sukses)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-103, 104, 105, 106, 107). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (58 langkah). Alasan: seluruh spec adalah satu topik (menutup form Add Stock manual) dan tiap kejadian menutup form butuh form baru (prinsip 6 bagian 3): 5 kali buka form (langkah 4, 9, 21, 33, 46) untuk 5 kejadian menutup form (langkah 6, 17, 30, 41, 54); tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC di spec berbeda dari nomor TC: TC-103 (form kosong, tanpa dialog) lebih dulu, lalu TC-105, TC-104, TC-106, dan TC-107 paling akhir karena TC-107 menyimpan satu unit (aksi yang mengubah data di akhir, prinsip 5). Urutan TC-105, TC-104, TC-106 adalah pilihan spec tanpa ketergantungan data.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, 19, 44), baseline (langkah 2), `[Add Stock]` toolbar sebagai pembuka form baru sesudah mendarat di Tab Available (langkah 9, 33), dan klik menu Hardware > Stock pada sidebar (langkah 43). Dialog Unsaved Changes pada langkah 16, 25, 29, 36, 40 adalah `Verifikasi` wajib S-08.
- Langkah 22 dan 47 membuktikan Expected "input dibuang" lewat form baru yang kosong; Expected TC-105 butir c dan TC-106 butir c menyebut input dibuang tanpa langkah observasi lain.
- Langkah 54 sampai 58 menambah Submit sukses dan F5 setelahnya untuk Expected TC-107 butir c ("setelah Submit sukses guard dilepas"); langkah TC-107 sendiri tidak memuat Submit.
- Temuan untuk QA:
  - TC-106 menyebut "menu lain di sidebar" tanpa menyebut menu mana; spec memakai menu `Approvals`.
  - TC-107 butir c (guard dilepas setelah Submit sukses) tidak punya langkah Submit atau F5 di TC; spec menambahkannya dan menafsirkan "guard dilepas" sebagai F5 tanpa konfirmasi sesudah redirect.
  - TC-107 menyebut "Buka Add Stock lagi" sesudah F5 pada form kosong; spec melanjutkan form yang sama karena F5 memuat ulang rute Add Stock.
  - TC-103, 104, 105, 106, 107 tidak memuat Post Condition.
