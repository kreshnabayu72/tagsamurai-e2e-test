---
id: TC-FA-TDC-E2E-224-bypass-ui-create-building-dan-land-ditolak-server-dan-rate-klien-diabaikan
title: "Bypass UI Create: Building dan Land Ditolak Server serta Rate dari Klien Diabaikan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-160
  - TC-FA-TDC-161
  - TC-FA-TDC-850
coverage:
  web: automated
---

# Bypass UI Create: Building dan Land Ditolak Server serta Rate dari Klien Diabaikan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, serta seed dan pemulihan lewat API. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Kemampuan intercept: `Spectra.intercept()` di atas backend nyata untuk mengganti payload request Create yang dikirim Drawer Add Tax Depreciation Class; intercept dilepas segera setelah pemicu selesai (S-09).
- Data milik spec (hook `before` memastikan tidak ada class `KHS-B1`, `KHS-L1`, dan `NB-9` lewat API; hook `after` menghapus ketiganya bila terbentuk; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsB1` | `KHS-B1` | belum ada di daftar; Class Name `Bangunan uji validasi`, Asset Type Building, Useful Life 20, Allowed Methods Straight Line |
| `khsL1` | `KHS-L1` | belum ada di daftar; Class Name `Tanah uji validasi`, Asset Type Land |
| `nb9` | `NB-9` | belum ada di daftar; dibuat langkah 35 |

- Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`) untuk Create lewat Drawer. Master Data Count Limit belum tercapai.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-160: Create Building dengan Declining Balance yang lolos dari UI ditolak server

1. Klik `+ Class` di toolbar
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `KHS-B1`
4. Isi Class Name `Bangunan uji validasi`
5. Pilih Asset Type `Building`
6. Isi Useful Life `20`
7. Pilih Allowed Methods `Straight Line`
8. Aktifkan intercept request Create: ganti payload Allowed Methods menjadi `Straight Line, Declining Balance`
9. Klik `[Submit]`
10. Lepas intercept request Create
11. Verifikasi caption error "Declining balance does not apply to buildings." tampil di bawah field Allowed Methods
12. Verifikasi Drawer tetap terbuka dengan input dipertahankan: Class Code `KHS-B1`, Class Name `Bangunan uji validasi`, Asset Type `Building`, Useful Life `20`
13. Klik `[×]` pada header Drawer
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`
16. Baca ulang daftar class lewat request baca
17. Verifikasi daftar class memuat sedikitnya satu class lain
18. Verifikasi class `KHS-B1` tidak ada di daftar

### TC-FA-TDC-161: Create Land dengan Useful Life atau Allowed Methods terisi yang lolos dari UI ditolak server

19. Klik `+ Class` di toolbar
20. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
21. Isi Class Code `KHS-L1`
22. Isi Class Name `Tanah uji validasi`
23. Pilih Asset Type `Land`
24. Aktifkan intercept request Create: ganti payload Useful Life menjadi `10` dan Allowed Methods menjadi `Straight Line`
25. Klik `[Submit]`
26. Lepas intercept request Create
27. Verifikasi caption error "Land is not depreciated." tampil di bawah field terkait (Useful Life atau Allowed Methods yang terisi)
28. Verifikasi Drawer tetap terbuka dengan input dipertahankan: Class Code `KHS-L1`, Class Name `Tanah uji validasi`, Asset Type `Land`
29. Klik `[×]` pada header Drawer
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`
32. Baca ulang daftar class lewat request baca
33. Verifikasi daftar class memuat sedikitnya satu class lain
34. Verifikasi class `KHS-L1` tidak ada di daftar

### TC-FA-TDC-850: Rate yang dikirim klien diabaikan dan rate dihitung server

35. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line` dan `Declining Balance`) dengan nilai Straight Line Rate `99` dan Declining Balance Rate `99` pada payload, hingga class tersimpan
36. Baca ulang class `NB-9` lewat request baca
37. Verifikasi class `NB-9` tersimpan dengan Straight Line Rate `10` dan Declining Balance Rate `20` hasil hitung server
38. Verifikasi nilai `99` dari payload tidak tersimpan pada Straight Line Rate dan Declining Balance Rate

## Notes

- K-1: TC kelas a dengan payload yang dimanipulasi tetap masuk spec FE+BE. TC-FA-TDC-160 dan TC-FA-TDC-161 berjalan lewat UI dengan intercept atas payload sehingga caption error Drawer diasersi; TC-FA-TDC-850 adalah request langsung dengan asersi respons dan state data lewat request baca (8b.1).
- Spec melewati sekitar 35 langkah (38). Alasan: seluruh blok satu kelas (kelas a) dan satu topik (server menolak atau mengabaikan nilai yang melewati validasi UI); menutup Drawer dirty (langkah 13 sampai 15 dan 29 sampai 31) wajib deterministik (S-08) sehingga tidak dapat dipadatkan; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Klausa Expected c TC-FA-TDC-160 dan TC-FA-TDC-161 menyebut "tidak ada class tersimpan dan tidak ada entri log"; bagian "tidak ada class tersimpan" diasersi langkah 18 dan 34 (didahului anchor positif langkah 17 dan 33), sedangkan bagian "tidak ada entri log" tidak diasersi di spec ini; asersinya ada di spec absence 263 dengan aksi nyata dan baseline sendiri per TC (S-05).
- Langkah penghubung (S-03): langkah 16 dan 32 (membaca daftar class lewat request baca); langkah 36 (membaca state data lewat request baca).
- Temuan untuk QA:
  - TC-FA-TDC-160 langkah 3 menawarkan dua cara ("suntikkan lewat DOM" atau "kirim ulang request dengan payload"); spec memakai intercept atas request Create yang dikirim `[Submit]`. Hal yang sama untuk TC-FA-TDC-161 langkah 3.
  - TC-FA-TDC-160 dan TC-FA-TDC-161 menyebut "Isi Regulation Reference" tanpa nilai; spec memakai `UU HPP 7/2021; PMK 72/2023` dari fixture.
  - TC-FA-TDC-850 tidak menyebut Class Name dan Regulation Reference pada request; spec mengirim field yang disebut TC saja.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
