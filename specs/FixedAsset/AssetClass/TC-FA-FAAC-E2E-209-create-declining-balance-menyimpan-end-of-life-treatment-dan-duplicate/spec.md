---
id: TC-FA-FAAC-E2E-209-create-declining-balance-menyimpan-end-of-life-treatment-dan-duplicate
title: "Create Asset Class Declining Balance: End-of-Life Treatment Nilai Awal, Charge in Final Period, Keep Depreciating, dan Tersalin Lewat Duplicate"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-720
  - TC-FA-FAAC-721
  - TC-FA-FAAC-727
sourceRules: ["FLD-33", "FAAC-LOGIC-02h", "FAAC-LOGIC-02i", "F-FAAC-01", "F-FAAC-06"]
smoke: []
dependsOn: []
trace:
  "FLD-33": [11, 22, 33, 41, 51]
  "FAAC-LOGIC-02h": [8, 11, 22, 33, 41, 51]
  "FAAC-LOGIC-02i": [22, 33]
  "F-FAAC-01": [5, 17, 28]
  "F-FAAC-06": [37, 39, 40, 41, 42, 43, 51]
coverage:
  web: automated
---

# Create Asset Class Declining Balance: End-of-Life Treatment Nilai Awal, Charge in Final Period, Keep Depreciating, dan Tersalin Lewat Duplicate

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup bernama literal (seed idempotent oleh fixture BE): plan Multi Depreciation (Enterprise) dengan Max depreciation methods minimal 2 dan Asset Class lain memakai `Straight Line`; Tax Depreciation Class `Bukan bangunan – Kelompok 1` Active (mengizinkan `Straight Line` dan `Declining Balance`); Asset Class `B-EOLDUP` (aktif; Method `Declining Balance`, Useful Life 48, Declining Rate 50, End-of-Life Treatment `Keep depreciating`, Tax Depreciation Class `Bukan bangunan – Kelompok 1` Active, Tax Method `Declining Balance`) sebagai sumber Duplicate; hanya dibaca. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Data yang dibuat spec (nama literal dari TC): Asset Class `B-EOLDEF` (Class Name `EOL Default`), `B-EOLCHG` (`EOL Charge`), `B-EOLKEEP` (`EOL Keep`), dan `B-EOLDUP2` (`EOL Dup Copy`). Keempat Class Code belum ada sebelum spec (precondition TC-720 dan TC-721); fixture BE menghapusnya bila ada di hook `before`. Hook `after` menghapus keempatnya lewat fixture BE (pembersihan tidak mengandalkan setup berhasil penuh).
- Data Dinamis: tidak ada yang bersuffix; Class Code dibatasi 15 karakter dan asersi TC bergantung pada nama (lihat Notes).
- Kemampuan teknis (disediakan tim FE/BE): fixture BE untuk seed, penghapusan Asset Class, dan pemulihan.
- State global: tidak ada selain Asset Class di atas; form Create dibiarkan dalam keadaan tersimpan (tidak ada form dirty di akhir spec).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-FAAC-720: Create Asset Class Declining Balance menyimpan End-of-Life Treatment nilai awal Switch to straight-line

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Pada tab General isi Class Code `B-EOLDEF`, Class Name `EOL Default`
3. Pada tab Depreciation pilih Method `Declining Balance`; isi Useful Life `48` dan Declining Rate `50`; biarkan End-of-Life Treatment tanpa diubah; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 1` lalu Tax Method `Declining Balance`; biarkan Tax Depreciation Start Rule bernilai awal `Month of expenditure`
4. Klik `Submit`
5. Verifikasi toast sukses `Success, asset class has been created.`
6. Klik breadcrumb `Asset Class`
7. Ketik Search `B-EOLDEF`, tekan Enter
8. Verifikasi kolom Commercial baris `B-EOLDEF` tetap `Declining Balance · 4 yrs · 50%/yr` tanpa teks End-of-Life Treatment
9. Klik link Class Code `B-EOLDEF` di tabel
10. Klik tab `Depreciation`
11. Verifikasi End-of-Life Treatment `Switch to straight-line`

### TC-FA-FAAC-721: Create Asset Class Declining Balance dengan opsi End-of-Life Treatment Charge in final period dan Keep depreciating

12. Klik breadcrumb `Asset Class`
13. Klik tombol `+ Asset Class` di toolbar tabel
14. Pada tab General isi Class Code `B-EOLCHG`, Class Name `EOL Charge`
15. Pada tab Depreciation pilih Method `Declining Balance`; isi Useful Life `48` dan Declining Rate `50`; pilih End-of-Life Treatment `Charge in final period`; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 1` lalu Tax Method `Declining Balance`; biarkan Tax Depreciation Start Rule bernilai awal `Month of expenditure`
16. Klik `Submit`
17. Verifikasi toast sukses `Success, asset class has been created.`
18. Klik breadcrumb `Asset Class`
19. Ganti isi kotak search dengan `B-EOLCHG`, tekan Enter
20. Klik link Class Code `B-EOLCHG` di tabel
21. Klik tab `Depreciation`
22. Verifikasi End-of-Life Treatment `Charge in final period`
23. Klik breadcrumb `Asset Class`
24. Klik tombol `+ Asset Class` di toolbar tabel
25. Pada tab General isi Class Code `B-EOLKEEP`, Class Name `EOL Keep`
26. Pada tab Depreciation pilih Method `Declining Balance`; isi Useful Life `48` dan Declining Rate `50`; pilih End-of-Life Treatment `Keep depreciating`; pilih Tax Depreciation Class `Bukan bangunan – Kelompok 1` lalu Tax Method `Declining Balance`; biarkan Tax Depreciation Start Rule bernilai awal `Month of expenditure`
27. Klik `Submit`
28. Verifikasi toast sukses `Success, asset class has been created.`
29. Klik breadcrumb `Asset Class`
30. Ganti isi kotak search dengan `B-EOLKEEP`, tekan Enter
31. Klik link Class Code `B-EOLKEEP` di tabel
32. Klik tab `Depreciation`
33. Verifikasi End-of-Life Treatment `Keep depreciating`

### TC-FA-FAAC-727: Duplicate Asset Class Declining Balance menyalin End-of-Life Treatment

34. Klik breadcrumb `Asset Class`
35. Ganti isi kotak search dengan `B-EOLDUP`, tekan Enter
36. Klik ikon `⋯` pada baris `B-EOLDUP` lalu pilih `Duplicate`
37. Verifikasi Detail mode Create terbuka dengan judul `Add Asset Class`
38. Klik tab `Depreciation`
39. Verifikasi Method `Declining Balance` tersalin dari sumber
40. Verifikasi Declining Rate `50` tersalin dari sumber
41. Verifikasi End-of-Life Treatment `Keep depreciating` tersalin dari sumber
42. Verifikasi Tax Depreciation Class `Bukan bangunan – Kelompok 1` ikut tersalin
43. Verifikasi Tax Method `Declining Balance` ikut tersalin
44. Klik tab `General`, isi Class Code `B-EOLDUP2` dan Class Name `EOL Dup Copy`
45. Klik `Submit`
46. Tunggu aksi selesai
47. Klik breadcrumb `Asset Class`
48. Ganti isi kotak search dengan `B-EOLDUP2`, tekan Enter
49. Klik link Class Code `B-EOLDUP2` di tabel
50. Klik tab `Depreciation`
51. Verifikasi End-of-Life Treatment `Keep depreciating`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-720, 721, 727). Tidak ada TC hanya-BE di spec ini.
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Class Code dan Class Name `B-EOLDEF`, `B-EOLCHG`, `B-EOLKEEP`, `B-EOLDUP2` ditulis literal tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama dan Class Code dibatasi 15 karakter; `B-EOLDUP` adalah seed bertanda `B-*` per TC yang hanya dibaca. Seed idempotent dan pembersihan oleh fixture BE di hook `before` dan `after`.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 6, 12, 18, 23, 29, 34, dan 47 (kembali ke tabel lewat breadcrumb; Detail tetap di mode Edit sesudah Submit); langkah 7, 19, 30, 35, dan 48 (Search untuk menemukan baris target, R-16 dan bagian 8b butir 13; "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah breadcrumb); langkah 46 ("Tunggu aksi selesai" sesudah `Submit` yang hasilnya tidak diasersi langsung, sebelum berpindah surface, bagian 8b butir 8); langkah 44 (mengisi Class Code dan Class Name pada tab General sesuai langkah 3 TC-727).
- Urutan langkah 8 dan 9 sampai 11 mengikuti urutan state (bagian 8b butir 5): kolom Commercial pada tabel (Expected TC-720 butir c) diasersi sebelum Detail dibuka, sedangkan Expected TC memuatnya sesudah butir b.
- Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah; ketiga blok TC satu topik (Create Declining Balance yang menyimpan End-of-Life Treatment) dan masing-masing memakai Class Code dan seed sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah pengisian sudah dipadatkan per tab seperti urutan langkah TC.
- Jalur Create Duplicate (TC-727) memakai `B-EOLDUP` hanya sebagai sumber salinan; baris sumber tidak diubah.
- Temuan untuk QA: (a) TC-720 dan TC-721 mensyaratkan plan Multi Depreciation dengan Max depreciation methods minimal 2 karena Asset Class lain memakai Straight Line; spec memakai satu client Enterprise. (b) TC-727 tidak menyebut toast sukses pada Submit; spec tidak mengasersinya dan menunggu aksi selesai (langkah 46). (c) TC-720 butir b menyebut Detail `B-EOLDEF` tab Depreciation tanpa menyebut Declining Rate; hanya End-of-Life Treatment yang diasersi.
