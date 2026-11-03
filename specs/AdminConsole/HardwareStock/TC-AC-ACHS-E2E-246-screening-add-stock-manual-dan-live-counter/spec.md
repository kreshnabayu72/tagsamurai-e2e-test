---
id: TC-AC-ACHS-E2E-246-screening-add-stock-manual-dan-live-counter
title: "Screening Add Stock Manual dan Live Counter Serial Numbers"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-76
  - TC-AC-ACHS-77
  - TC-AC-ACHS-78
  - TC-AC-ACHS-79
  - TC-AC-ACHS-115
coverage:
  web: automated
---

# Screening Add Stock Manual dan Live Counter Serial Numbers

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{deviceNameFx}` | #16 Tabel A baris 3 | Device Name SKU Smart Fixed Reader | `Fixture.hardwareStock.p16.a[3].deviceName` |
| `{brandFx}` | #16 Tabel A baris 3 | Brand SKU Smart Fixed Reader | `Fixture.hardwareStock.p16.a[3].brand` |
| `{modelFx}` | #16 Tabel A baris 3 | Model/Type SKU Smart Fixed Reader | `Fixture.hardwareStock.p16.a[3].modelType` |
| `{skuBle}` | #16 Tabel A baris 5; #27 | kode SKU BLE Gateway, 4 Available dan 1 In Use, Brand dan Model/Type 25 karakter atau kurang | `Fixture.hardwareStock.p16.a[5].sku` |
| `{deviceNameBle}` | #16 Tabel A baris 5 | Device Name SKU BLE Gateway | `Fixture.hardwareStock.p16.a[5].deviceName` |
| `{brandBle}` | #16 Tabel A baris 5 | Brand SKU BLE Gateway | `Fixture.hardwareStock.p16.a[5].brand` |
| `{modelBle}` | #16 Tabel A baris 5 | Model/Type SKU BLE Gateway | `Fixture.hardwareStock.p16.a[5].modelType` |

- Data Pre-setup: SKU `{skuFx}` (Smart Fixed Reader) dan SKU `{skuBle}` (BLE Gateway) dari Pre-setup #16 dan unit Pre-setup #27; atribut katalog (Device Name, Brand, Model/Type) dibaca lewat parameter atribut pada tabel Parameter Pre-setup. Keduanya hanya dibuka; satu unit baru dibuat pada SKU {skuFx} di langkah 39.
- Data Dinamis: Serial Number unit yang disimpan diberi suffix per run: `SN-AUTO-0001-{runId}-246`. Nilai yang diketik hanya untuk live counter (`SN-CNT-0001` s.d. `SN-CNT-0003`, dua baris kosong, satu baris spasi, dan dua baris pada TC-79) tidak pernah disimpan sehingga literal seperti di TC.
- Kemampuan teknis (disediakan tim FE/BE): membaca Registered At unit baru dan waktu Submit dengan jam server dan jam browser yang sinkron (toleransi satu menit); fixture BE yang menghapus unit bersuffix `-{runId}-246` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA); membaca atribut ARIA elemen (`aria-describedby`).
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU `{skuFx}` berubah selama spec berjalan (SKU Pre-setup tidak dapat dimiliki spec karena katalog dan fotonya Pre-setup #16); unit baru dihapus hook `after`, baris SKU dicatat sebelum aksi (baseline) dan diasersi dengan selisih.

## Test Steps

### TC-AC-ACHS-77: Screening halaman Add Stock manual SKU {skuBle}

1. Ketik Search `{skuBle}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuBle}`
3. Klik opsi `Add Stock`
4. Verifikasi Breadcrumb `Hardware > Stock > Add Stock`
5. Verifikasi Page Header `Add Stock — {skuBle}`
6. Verifikasi SKU Info Card (read-only) memuat Foto, `{deviceNameBle}`, `{brandBle}`, `{modelBle}`, dan badge `BLE Gateway` tanpa badge Range Type
7. Verifikasi Card Serial Numbers: label `Serial Numbers *`, textarea (expandable) dengan placeholder `Enter one serial number per line`
8. Verifikasi helper `Each line = one unit. Duplicates will be flagged before saving.`
9. Verifikasi tidak ada field Date Received maupun Notes
10. Verifikasi Footer (sticky) memuat `[Cancel]` (text, contrast) dan `[Submit]` (filled, success)
11. Klik segmen `Stock` pada breadcrumb (form bersih, kembali ke Stock List)

### TC-AC-ACHS-76: Screening halaman Add Stock manual SKU Smart Fixed Reader

12. Ketik Search `{skuFx}`, tekan Enter
13. Catat Total Registered, Available, dan In Use pada baris SKU `{skuFx}` sebagai baseline
14. Klik `(⋯)` pada baris SKU `{skuFx}`
15. Klik opsi `Add Stock`
16. Verifikasi Breadcrumb `Hardware > Stock > Add Stock`
17. Verifikasi Page Header `Add Stock — {skuFx}`
18. Verifikasi SKU Info Card (read-only) memuat Foto, `{deviceNameFx}`, `{brandFx}`, `{modelFx}`, dan badge `Smart Fixed Reader` tanpa badge Range Type
19. Verifikasi Card Serial Numbers: label `Serial Numbers *`, textarea (expandable) dengan placeholder `Enter one serial number per line`
20. Verifikasi helper `Each line = one unit. Duplicates will be flagged before saving.`
21. Verifikasi tidak ada field Date Received maupun Notes
22. Verifikasi Footer (sticky) memuat `[Cancel]` (text, contrast) dan `[Submit]` (filled, success)

### TC-AC-ACHS-78: Live counter textarea Serial Numbers

23. Ketik `SN-CNT-0001` di textarea
24. Verifikasi counter menampilkan "1 serial number detected"
25. Tekan Enter dan ketik `SN-CNT-0002`, tekan Enter lalu ketik `SN-CNT-0003`
26. Verifikasi counter menampilkan "3 serial numbers detected"
27. Tambahkan dua baris kosong dan satu baris berisi spasi
28. Verifikasi counter tetap menampilkan "3 serial numbers detected"

### TC-AC-ACHS-79: Accessibility textarea Serial Numbers

29. Kosongkan textarea, lalu ketik dua baris `SN-ARIA-0001` dan `SN-ARIA-0002`
30. Verifikasi textarea Serial Numbers punya atribut `aria-describedby` yang menunjuk elemen counter
31. Verifikasi teks elemen yang dirujuk `aria-describedby` berubah menjadi "2 serial numbers detected"
32. Klik `[Cancel]`
33. Verifikasi dialog Unsaved Changes tampil dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
34. Klik `[Leave]`

### TC-AC-ACHS-115: Form tidak memiliki Date Received dan Notes, waktu terima dicatat otomatis

35. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuFx}` (form baru)
36. Verifikasi satu-satunya input pada form adalah textarea Serial Numbers
37. Verifikasi tidak ada Date Received maupun Notes
38. Ketik `SN-AUTO-0001-{runId}-246` di textarea
39. Klik `[Submit]`
40. Catat waktu sesudah Submit
41. Verifikasi Registered At unit `SN-AUTO-0001-{runId}-246` pada Tab Available berisi waktu Submit mengikuti format General Settings (selisih waktu kurang dari satu menit)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-76, 77, 78, 79, 115). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di spec berbeda dari nomor TC: TC-77 (form bersih BLE) lebih dulu, lalu TC-76, TC-78, TC-79 (form menjadi dirty), dan TC-115 (butuh form baru). Alasannya: menutup form dirty memerlukan dialog Unsaved Changes (S-08), jadi form bersih dipakai lebih dulu dan form baru dibuka untuk TC-115 (prinsip 6). Jumlah buka form: 3 (SKU {skuBle}, SKU {skuFx}, SKU {skuFx} form baru), sejalan dengan 3 kejadian menutup form (langkah 11, 32 sampai 34, 39).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search SKU untuk menemukan baris target (langkah 1 dan 12), pembukaan form baru lewat `[Add Stock]` toolbar Tab Available (langkah 35, bukan row action karena `[Leave]` mendarat di Tab Available), langkah 13 (baseline), pengosongan textarea sebelum TC-79 (langkah 29), `[Cancel]` dan `[Leave]` penutup form dirty (langkah 32 sampai 34), dan pencatatan waktu (langkah 40). Dialog Unsaved Changes pada langkah 33 adalah `Verifikasi` wajib S-08.
- Spec di atas smell 35 langkah (41 langkah). Alasan: lima TC satu kelas (form Add Stock manual, satu SKU) yang berurutan karena form dirty harus ditutup lewat dialog Unsaved Changes sebelum form baru; dipecah akan menggandakan Search dan pembukaan form.
- Langkah 36 dan 37 mengulang cek yang sama dengan langkah 9 dan 21 (TC-115 dan TC-76 memuat butir yang sama pada form berbeda); TC-115 punya Expected sendiri.
- Baseline langkah 13 dipakai untuk menjaga selisih hitungan pada Stock List sesudah unit dibuat dihapus hook `after`; spec ini tidak mengasersi hitungan karena Expected TC-76, 77, 78, 79, dan 115 tidak memintanya.
- Temuan untuk QA:
  - TC-79 butir a menyebut `aria-describedby` menunjuk "elemen counter" tanpa menyebut apakah elemen itu ada saat textarea kosong; spec mengasersi atribut setelah dua baris diketik.
  - TC-115 langkah 6 ("Amati Registered At pada Tab Available") tidak menyebut redirect setelah Submit; spec mengasersi Tab Available setelah redirect yang dinyatakan TC-80.
  - TC-115 tidak punya Post Condition; TC-78 dan TC-79 juga tidak.
  - Pemicu hapus unit bersuffix di hook `after` tidak didefinisikan di TC, PRD, atau LLD yang dibaca; disediakan tim FE/BE.
