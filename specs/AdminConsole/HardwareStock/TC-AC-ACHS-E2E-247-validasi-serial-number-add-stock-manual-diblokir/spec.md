---
id: TC-AC-ACHS-E2E-247-validasi-serial-number-add-stock-manual-diblokir
title: "Validasi Serial Number Add Stock Manual Diblokir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-84
  - TC-AC-ACHS-88
  - TC-AC-ACHS-89
  - TC-AC-ACHS-90
  - TC-AC-ACHS-91
  - TC-AC-ACHS-92
  - TC-AC-ACHS-96
coverage:
  web: automated
---

# Validasi Serial Number Add Stock Manual Diblokir

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{skuBle}` | #16 Tabel A baris 5; #27 | kode SKU BLE Gateway, 4 Available dan 1 In Use, Brand dan Model/Type 25 karakter atau kurang | `Fixture.hardwareStock.p16.a[5].sku` |
| `{snCakraFx}` | #27 | Serial Number unit Available pertama SKU Smart Fixed Reader milik Distributor Pre-setup #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `{snCakraFxLower}` | #27 (turunan) | `{snCakraFx}` dalam huruf kecil | `Fixture.hardwareStock.derived.cakraFxSerialLower` |
| `{macBleInUse}` | #27 | MAC Address unit In Use SKU BLE Gateway | `Fixture.hardwareStock.p27.ble[1].identifier` |

- Data Pre-setup (hanya dibaca, tidak diubah): SKU `{skuFx}` dengan unit Available `{snCakraFx}` (Pre-setup #27) dan SKU `{skuBle}` dengan unit In Use `{macBleInUse}` (Pre-setup #27). Serial Number lain yang diketik (`SN-DUP-0001`, `SN-DUP-0002`, `SN-CASE-0001`, SN 121 karakter) selalu diblokir sehingga tidak ada data yang dibuat dan nilainya literal seperti di TC.
- Data Dinamis: tidak ada. Spec ini tidak membuat unit, sehingga tidak ada pembersihan.
- Baseline hitungan: Total Registered, Available, dan In Use kedua SKU dicatat dari Stock List sebelum aksi (langkah 2 dan 4) untuk membuktikan tidak ada unit tersimpan.
- Kemampuan teknis: tidak ada tambahan di luar hook suite.

## Test Steps

### Persiapan baseline

1. Ketik Search `{skuFx}`, tekan Enter
2. Catat Total Registered, Available, dan In Use baris SKU `{skuFx}` sebagai baseline {skuFx}
3. Ketik Search `{skuBle}`, tekan Enter
4. Catat Total Registered, Available, dan In Use baris SKU `{skuBle}` sebagai baseline {skuBle}
5. Ketik Search `{skuFx}`, tekan Enter
6. Klik `(⋯)` pada baris SKU `{skuFx}`
7. Klik opsi `Add Stock`

### TC-AC-ACHS-84: Serial Numbers kosong

8. Biarkan textarea kosong, klik `[Submit]`
9. Verifikasi error banner "Serial numbers must not be empty" tampil setelah Submit
10. Ketik tiga baris berisi spasi saja, klik `[Submit]`
11. Verifikasi error banner yang sama "Serial numbers must not be empty" tampil untuk input baris spasi

### TC-AC-ACHS-96: Serial Number 121 karakter

12. Kosongkan isi textarea
13. Tempel satu baris Serial Number sepanjang 121 karakter (`SN-LEN121-` + 111 karakter `A`)
14. Verifikasi error banner real-time "Max. 120 characters" tampil
15. Verifikasi `[Submit]` diblokir

### TC-AC-ACHS-88: Duplikat dalam satu batch

16. Kosongkan isi textarea
17. Ketik empat baris `SN-DUP-0001`, `SN-DUP-0002`, `SN-DUP-0001`, `SN-DUP-0002`
18. Verifikasi error banner real-time "Duplicate serial numbers found: SN-DUP-0001, SN-DUP-0002. Each serial number must be unique."
19. Verifikasi `[Submit]` diblokir

### TC-AC-ACHS-89: Duplikat intra-batch tidak membedakan huruf besar-kecil setelah trim

20. Kosongkan isi textarea
21. Ketik dua baris `SN-CASE-0001` dan `  sn-case-0001  `
22. Verifikasi error banner V-04 "Duplicate serial numbers found:" tampil
23. Verifikasi `[Submit]` diblokir

### TC-AC-ACHS-90: Serial Number sudah ada berstatus Available pada SKU yang sama

24. Kosongkan isi textarea
25. Ketik `{snCakraFx}`
26. Klik `[Submit]`
27. Verifikasi error banner "Serial number {snCakraFx} already exists in the system"
28. Verifikasi form tetap terbuka (Breadcrumb `Hardware > Stock > Add Stock`) dan textarea masih berisi `{snCakraFx}`

### TC-AC-ACHS-92: Keunikan server tidak membedakan huruf besar-kecil dan spasi tepi

29. Kosongkan isi textarea
30. Ketik `  {snCakraFxLower}  `
31. Klik `[Submit]`
32. Verifikasi error banner V-05 "Serial number {snCakraFxLower} already exists in the system"

### Penutup form SKU {skuFx} dan bukti tidak ada unit tersimpan

33. Klik `[Cancel]`
34. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
35. Klik `[Leave]`
36. Verifikasi Summary bar Stock Detail SKU {skuFx}: Total Registered, Available, dan In Use sama dengan baseline langkah 2 (tidak ada unit tersimpan untuk TC-84, 88, 89, 90, 92, dan 96)

### TC-AC-ACHS-91: Serial Number sudah ada berstatus In Use pada SKU {skuBle}

37. Klik segmen `Stock` pada breadcrumb
38. Ketik Search `{skuBle}`, tekan Enter
39. Klik `(⋯)` pada baris SKU `{skuBle}`
40. Klik opsi `Add Stock`
41. Ketik `{macBleInUse}`
42. Klik `[Submit]`
43. Verifikasi error banner "Serial number {macBleInUse} already exists in the system"
44. Verifikasi form tetap terbuka (Breadcrumb `Hardware > Stock > Add Stock`)
45. Klik `[Cancel]`
46. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
47. Klik `[Leave]`
48. Verifikasi Summary bar Stock Detail SKU {skuBle}: Total Registered, Available, dan In Use sama dengan baseline langkah 4 (tidak ada unit tersimpan untuk TC-91)

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-84, 88, 89, 90, 91, 92, 96). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (48 langkah). Alasan: semua blok adalah validasi yang diblokir pada satu form Add Stock yang sama (halaman yang sama dipakai berulang, prinsip 13 bagian 3) dengan textarea dikosongkan di antara kasus; tidak ada data yang dibuat sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna (soft assertion).
- Urutan kasus: validasi sisi klien (TC-84, 96, 88, 89) lebih dulu, lalu validasi server (TC-90, 92), lalu TC-91 pada SKU {skuBle} di form baru (beda SKU). Buka form 2 kali dan menutup form 2 kali (langkah 33 sampai 35 dan 45 sampai 47).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, 3, 5, 38), pencatatan baseline (langkah 2, 4), pengosongan textarea di antara kasus (langkah 12, 16, 20, 24, 29), serta `[Cancel]` dan `[Leave]` (langkah 33, 35, 45, 47) dan klik breadcrumb (langkah 37). Dialog Unsaved Changes (langkah 34, 46) adalah `Verifikasi` wajib S-08.
- Expected "tidak ada unit tersimpan" (TC-84 b, 88 b, 90 c, 91 b, 92 b, 96 b) tidak dapat diamati di dalam form yang memblokir Submit; dibuktikan sekali per SKU sesudah form ditutup dengan selisih terhadap baseline (langkah 36 dan 48), bukan setelah tiap TC.
- Banner V-04 pada langkah 18 ditulis dengan nilai konkret: TC-88 menuliskan templat `[SN1], [SN2]` dan nilai konkretnya.
- Temuan untuk QA:
  - TC-84 butir a menyebut banner muncul "setelah Submit", sedangkan TC-96, 88, dan 89 menyebut banner real-time; TC tidak menyatakan apakah banner TC-84 hilang saat textarea diisi, sehingga spec tidak mengasersi hilangnya banner.
  - TC-89 tidak menyebut daftar nilai duplikat pada banner V-04; spec hanya mengasersi awalan `Duplicate serial numbers found:` seperti di TC.
  - TC-92 mengharapkan banner memuat nilai yang diketik setelah trim dengan huruf kecil; TC tidak menyatakan apakah nilai pada banner di-trim atau tidak (spec menuliskan nilai tanpa spasi tepi).
