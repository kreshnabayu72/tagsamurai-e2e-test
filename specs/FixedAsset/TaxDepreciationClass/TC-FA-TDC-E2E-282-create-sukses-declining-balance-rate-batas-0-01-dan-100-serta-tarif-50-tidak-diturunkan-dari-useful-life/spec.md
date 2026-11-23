---
id: TC-FA-TDC-E2E-282-create-sukses-declining-balance-rate-batas-0-01-dan-100-serta-tarif-50-tidak-diturunkan-dari-useful-life
title: "Create Sukses: Declining Balance Rate Batas Valid 0.01 dan 100 serta Tarif 50 pada Useful Life 10 Tersimpan Apa Adanya"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-937
  - TC-FA-TDC-938
sourceRules: ["V-17", "FATDC-LOGIC-03f.2", "§9.9", "FLD-08", "N-19"]
smoke: []
dependsOn: []
trace:
  "V-17": [4, 10]
  "FATDC-LOGIC-03f.2": [3, 9, 14, 22, 31, 37, 40]
  "§9.9": [4, 10, 14, 22]
  "FLD-08": [32, 33, 37, 40]
  "N-19": [32, 33, 37, 40]
coverage:
  web: automated
---

# Create Sukses: Declining Balance Rate Batas Valid 0.01 dan 100 serta Tarif 50 pada Useful Life 10 Tersimpan Apa Adanya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Master Data Count Limit belum tercapai (Precondition c kedua TC); kemampuan mengatur kuota disediakan tim FE/BE.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (dibuat lewat UI oleh spec; hook `before` menghapus sisa class berkode sama dari run sebelumnya lewat API dan hook `after` menghapus tiga class yang dibuat spec; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; awalan `DBE-` tidak dipakai TC lain; kemampuan seeding dan penghapusan lewat API disediakan tim FE/BE):

| Class Code | Class Name | Declining Balance Rate | Useful Life |
|---|---|---|---|
| `DBE-02` | `Kelompok uji tarif 2` | `0.01` | 8 |
| `DBE-03` | `Kelompok uji tarif 3` | `100` | 8 |
| `DBE-04` | `Kelompok uji tarif 4` | `50` | 10 |

  Nilai lain tiap class: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Asset Type `Non-building`, Allowed Methods `Declining Balance`. Class Code `DBE-02`, `DBE-03`, dan `DBE-04` belum ada pada awal spec.
- Tabel berisi lebih dari satu halaman setelah class dibuat (7 class seed ditambah tiga class milik spec), sehingga baris target dibuka lewat Search Class Code (8b.13, R-23).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-937: Submit Create dengan Declining Balance Rate batas valid 0.01 dan 100 diterima dan tersimpan

1. Klik `+ Class` di toolbar
2. Isi form valid dengan Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-02`, Class Name `Kelompok uji tarif 2`, pilih Asset Type `Non-building`, isi Useful Life `8`, pilih Allowed Methods `Declining Balance`
3. Isi Declining Balance Rate `0.01`
4. Verifikasi tidak ada caption error pada Declining Balance Rate `0.01`
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, tax depreciation class has been created."
7. Klik `+ Class` di toolbar
8. Isi form valid dengan Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-03`, Class Name `Kelompok uji tarif 3`, pilih Asset Type `Non-building`, isi Useful Life `8`, pilih Allowed Methods `Declining Balance`
9. Isi Declining Balance Rate `100`
10. Verifikasi tidak ada caption error pada Declining Balance Rate `100`
11. Klik `[Submit]`
12. Verifikasi toast sukses "Success, tax depreciation class has been created."
13. Ketik Search `DBE-02`, tekan Enter
14. Verifikasi baris `DBE-02`: Declining Balance Rate "0.01%" dan Straight Line Rate "—"
15. Klik link Class Code `DBE-02` pada tabel
16. Verifikasi badge Status "Active"
17. Klik tautan View versions
18. Verifikasi modal Versions memuat satu baris berstatus "Current" dengan Declining Balance Rate "0.01%"
19. Tutup modal Versions
20. Klik `[×]` pada Drawer Edit
21. Ganti isi kotak search dengan `DBE-03`, tekan Enter
22. Verifikasi baris `DBE-03`: Declining Balance Rate "100%" dan Straight Line Rate "—"
23. Klik link Class Code `DBE-03` pada tabel
24. Verifikasi badge Status "Active"
25. Klik tautan View versions
26. Verifikasi modal Versions memuat satu baris berstatus "Current" dengan Declining Balance Rate "100%"
27. Tutup modal Versions
28. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-938: Declining Balance Rate tersimpan apa adanya dan tidak diturunkan dari Useful Life (tarif 50 pada Useful Life 10)

29. Klik `+ Class` di toolbar
30. Isi form valid dengan Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-04`, Class Name `Kelompok uji tarif 4`, pilih Asset Type `Non-building`, isi Useful Life `10`, pilih Allowed Methods `Declining Balance`
31. Isi Declining Balance Rate `50`
32. Verifikasi helper "Equivalent to 5.0× the straight-line rate" (50 ÷ (100 ÷ 10) = 5.0)
33. Verifikasi nilai `50` diterima tanpa caption error (tidak dibatasi faktor 2×)
34. Klik `[Submit]`
35. Verifikasi toast sukses "Success, tax depreciation class has been created."
36. Ganti isi kotak search dengan `DBE-04`, tekan Enter
37. Verifikasi baris `DBE-04`: Straight Line Rate "—" dan Declining Balance Rate "50%"
38. Klik link Class Code `DBE-04` pada tabel
39. Klik tautan View versions
40. Verifikasi modal Versions memuat satu baris dengan Declining Balance Rate "50%"
41. Tutup modal Versions
42. Klik `[×]` pada Drawer Edit

## Notes

- Alasan melewati sekitar 35 langkah (42 langkah): kedua TC satu topik Create sukses dengan nilai Declining Balance Rate dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); tiap TC membuat class sendiri dan blok baca ulang per class (langkah 13 sampai 20, 21 sampai 28) berpola sama.
- Langkah penghubung (S-03): langkah 13, 21, dan 36 (Search Class Code untuk menemukan baris target; R-16; Search tidak dibersihkan di antara blok karena langkah berikutnya menggantinya dan dibersihkan oleh klik sidebar pada pembukaan layar spec berikutnya); langkah 19, 20, 27, 28, 41, dan 42 (menutup modal Versions dan Drawer Edit tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Spec ini tidak memuat asersi absence. Langkah 4 dan 10 menyalin Expected a TC-FA-TDC-937 ("tidak ada caption error pada kedua nilai") dan langkah 33 menyalin Expected b TC-FA-TDC-938; asersi tidak ada caption didahului pengisian nilai pada field yang sama (anchor: field terisi tampil).
- Urutan TC-FA-TDC-937: TC memisahkan "baca baris DBE-02 dan DBE-03" (langkah 4) dari "buka Drawer Edit" (langkah 5 dan 6); spec membaca baris dan Drawer per class dalam satu Search (langkah 13 sampai 28) karena Search menyaring tabel per kode.
- Asumsi: sesudah `[Submit]` yang sukses Drawer Create tertutup sehingga `+ Class` pada langkah 7 dan 29 membuka form baru (TC-FA-TDC-937 langkah 3 menulis "Klik `+ Class`" lagi); perlu konfirmasi FE.
- Temuan untuk QA:
  - TC-FA-TDC-937 menyebut "form valid" untuk kedua class dengan nilai yang sama kecuali Class Code, Class Name, dan Declining Balance Rate; spec mengisi satu langkah form valid dengan nilai TC.
  - TC-FA-TDC-937 Expected c menyebut Straight Line Rate "—" pada kedua class sedangkan Useful Life `8` terisi; spec mengikuti TC (Straight Line tidak diizinkan pada class ini).
  - TC-FA-TDC-937 dan TC-FA-TDC-938 Post Condition tidak punya langkah observasi sendiri selain Expected; tidak ada asersi tambahan (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
