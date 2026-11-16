---
id: TC-FA-TDC-E2E-047-create-validasi-class-name-kosong-panjang-dan-emoji
title: "Create - Validasi Class Name Kosong, Panjang, dan Emoji"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-144
  - TC-FA-TDC-145
  - TC-FA-TDC-146
  - TC-FA-TDC-147
  - TC-FA-TDC-148
sourceRules: ["V-05", "F-FATDC-01.k4b", "E-FATDC-04", "V-06", "V-07", "E-FATDC-03"]
smoke: []
dependsOn: []
trace:
  "V-05": [4, 7]
  "F-FATDC-01.k4b": 7
  "E-FATDC-04": [8, 9]
  "V-06": [12, 14]
  "V-07": [17, 18, 20, 21, 26]
  "E-FATDC-03": [27, 28]
coverage:
  web: automated
---

# Create - Validasi Class Name Kosong, Panjang, dan Emoji

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (semua Submit diblokir validasi). Data Uji dasar (field selain Class Name): Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Class Code uji `KHS-N1` dan `KHS-N2` (literal TC; Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; seeding idempotent, suite serial, kode berbeda antar spec). Nilai Class Name uji: kosong, tiga spasi, 121 karakter `A`, 120 karakter `A`, `😀`, `Uji 😀`.
- Kemampuan teknis: menyuntikkan nilai langsung ke DOM field Class Name (melewati filter keystroke FE; disediakan tim FE).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-144: Create - Class Name kosong atau hanya spasi ditolak

1. Klik `+ Class` di toolbar
2. Isi field lain sesuai Data Uji dasar dan Class Code `KHS-N1`; biarkan Class Name kosong
3. Klik `[Submit]`
4. Verifikasi caption "Class name must not be empty" muncul pada Class Name (Class Name kosong)
5. Isi Class Name dengan tiga spasi
6. Klik `[Submit]`
7. Verifikasi caption "Class name must not be empty" muncul pada Class Name (tiga spasi)
8. Verifikasi Drawer tetap terbuka
9. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)

### TC-FA-TDC-145: Create - Class Name 121 karakter ditolak saat mengetik

10. Klik `[Clear Field]`
11. Tempel 121 karakter `A` pada Class Name
12. Verifikasi caption "Max. 120 characters" muncul pada Class Name

### TC-FA-TDC-146: Create - Class Name tepat 120 karakter diterima

13. Ganti isi Class Name dengan 120 karakter `A`
14. Verifikasi tidak ada caption error pada Class Name

### TC-FA-TDC-147: Create - Emoji pada Class Name diblok saat diketik atau ditempel

15. Klik `[Clear Field]`
16. Ketik `😀` pada Class Name
17. Verifikasi karakter emoji tidak masuk ke nilai field Class Name (diketik)
18. Verifikasi tidak ada caption error pada Class Name (diketik)
19. Tempel `😀` pada Class Name
20. Verifikasi karakter emoji tidak masuk ke nilai field Class Name (ditempel)
21. Verifikasi tidak ada caption error pada Class Name (ditempel)

### TC-FA-TDC-148: Create - Emoji yang lolos filter input ditolak dengan pesan fallback

22. Klik `[Clear Field]`
23. Isi field lain sesuai Data Uji dasar dan Class Code `KHS-N2`
24. Suntikkan nilai `Uji 😀` langsung ke DOM field Class Name (bypass filter keystroke FE, simulasi drag-drop)
25. Klik `[Submit]`
26. Verifikasi caption "Class name contains invalid characters" muncul pada Class Name
27. Verifikasi Drawer tetap terbuka
28. Verifikasi tabel di belakang Drawer tetap berisi 7 class seed tanpa baris baru (tidak ada data tersimpan)
29. Klik `[Clear Field]`
30. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 10, 15, 22, dan 29 (`[Clear Field]` mengosongkan form dan caption sebelum kasus berikutnya atau sebelum menutup Drawer; S-09), langkah 13 ("Ganti isi" Class Name menggantikan 121 karakter sebelumnya), langkah 30 (menutup Drawer yang bersih).
- Satu pembukaan Drawer dipakai untuk seluruh kasus (prinsip 3, halaman yang sama dipakai berulang); kasus yang diblokir Submit diletakkan pada TC-FA-TDC-144 dan TC-FA-TDC-148.
- Asersi absence langkah 18 dan 21 didahului anchor positif langkah 17 dan 20 (field Class Name tampil tanpa emoji); asersi absence langkah 14 didahului anchor caption pada langkah 12.
- Langkah 16 dan 19 menjalankan "ketik" dan "tempel" sebagai dua aksi terpisah karena TC menyebut keduanya; Expected a dan b diasersi pada masing-masing.
- Pembagian TC lintas spec: validasi Class Name lain (trim dan duplikat diizinkan) ada di spec `TC-FA-TDC-E2E-048-create-class-name-trim-duplikat-diizinkan-dan-regulation-reference-kosong`.
- Temuan untuk QA:
  - TC-FA-TDC-147 Expected a dan b tidak menyebut perbedaan perilaku ketik dan tempel; spec mengasersi hasil yang sama untuk keduanya.
  - Post Condition TC-FA-TDC-144 sampai 148 ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi di TC; spec mengasersi data lewat jumlah baris tabel pada Expected c TC-FA-TDC-144 dan b TC-FA-TDC-148, dan tidak mengasersi entri log (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
