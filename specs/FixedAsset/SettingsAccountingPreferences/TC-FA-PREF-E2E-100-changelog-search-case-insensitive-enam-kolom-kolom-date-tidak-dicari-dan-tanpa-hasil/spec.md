---
id: TC-FA-PREF-E2E-100-changelog-search-case-insensitive-enam-kolom-kolom-date-tidak-dicari-dan-tanpa-hasil
title: "Changelog Search: Case-Insensitive pada Enam Kolom, Kolom Date Tidak Dicari, dan Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-300
  - TC-FA-PREF-301
  - TC-FA-PREF-302
coverage:
  web: automated
---

# Changelog Search: Case-Insensitive pada Enam Kolom, Kolom Date Tidak Dicari, dan Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PB-1; Changelog Preferences berisi 9 entri contoh PB-C1 (format tanggal dd/MM/yy dan 24 jam). Posisi baris pada urutan default Date Newest First (sama dengan TC-FA-PREF-290): baris 1 Edit Chart of Accounts Default Capitalization Offset (Budi S); baris 2 dan baris 3 Edit Disposal Disposal Documents — Sell dan — Scrap, Optional ke Required, Date 26/10/26 14:05 (Rina A); baris 4 Edit Journal Export Journal Grouping (Budi S); baris 5 Edit Disposal Default Gain on Disposal (Rina A); baris 6 Edit General Fiscal Year Start, January ke April (Rina A); baris 7 Edit General First Accounting Period, Mar 2026 ke Jan 2026 (Rina A); baris 8 Edit Capitalization Default Capitalization Threshold (Rina A); baris 9 Create Preferences, Initial values (Budi S). Urutan tulis seed: pada Date yang sama baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed PB-C1 mengatur Changelog company seed ke tepat 9 entri (lihat Temuan untuk QA).
- Tabel "Kata kunci huruf besar per kolom" (TC-FA-PREF-300; langkah 2 sampai 4 diulang untuk tiap baris tabel):

  | Kolom | Kata kunci | Baris yang tampil, berurutan |
  |---|---|---|
  | Action | CREATE | baris 9 |
  | Section | JOURNAL EXPORT | baris 4 |
  | Field | FISCAL | baris 6 |
  | Old Value | MAR 2026 | baris 7 |
  | New Value | REQUIRED | baris 2, baris 3 |
  | Modified By | BUDI | baris 1, baris 4, baris 9 |

- Spec ini tidak menulis ke Changelog; Search tidak mengubah state server.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik ikon View history di header tab Preferences

### TC-FA-PREF-300: Search tidak membedakan huruf besar dan kecil pada enam kolom searchable

2. Untuk setiap baris tabel "Kata kunci huruf besar per kolom" (langkah 2 sampai 4): ketik Search kata kunci huruf besar kolom itu, tekan Enter
3. Verifikasi tabel menampilkan baris yang tertera pada kolom "Baris yang tampil, berurutan" tabel itu
4. Kosongkan isi kotak search, tekan Enter

### TC-FA-PREF-301: Search tidak mencocokkan nilai kolom Date

5. Ketik Search "26/10/26", tekan Enter
6. Verifikasi tabel menampilkan empty state berjudul "No results found" dengan deskripsi "Try adjusting your search or filter."
7. Verifikasi baris dengan Date 26/10/26 tidak tampil
8. Kosongkan isi kotak search, tekan Enter

### TC-FA-PREF-302: Search tanpa hasil menampilkan empty state hasil kosong

9. Ketik Search "zzzz", tekan Enter
10. Verifikasi empty state menampilkan ilustrasi, judul "No results found", dan deskripsi "Try adjusting your search or filter."
11. Klik (←) pada kotak Search
12. Klik ikon [✕] di header modal Changelog

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 membuka modal satu kali untuk ketiga TC (precondition sama, tidak ada aksi yang mengubah state modal); langkah 4 dan 8 (mengosongkan kotak Search dan menyetel ulang tabel sebelum TC berikutnya); langkah 11 (menutup input Search dan mereset tabel, bagian 8b butir 9); langkah 12 (menutup modal). Langkah "Klik ikon Search" TC-FA-PREF-301 dan 302 dipenuhi langkah "Ketik Search" yang membuka input bila tertutup (bagian 8b butir 9).
- Langkah 2 sampai 4 diulang untuk enam baris tabel Prerequisites (bagian 8b butir 7); `Verifikasi` tetap satu per klausa Expected (S-01): satu per kata kunci. Dengan ekspansi spec ini 27 langkah.
- Langkah 7 (absence) memakai empty state pada langkah 6 sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-PREF-300 mengasersi posisi baris seed ("baris 9", "baris 2 lalu baris 3") yang bergantung pada Changelog tepat 9 entri seed; Changelog adalah audit trail permanen yang tumbuh karena Save pada spec lain (S-12, S-14). Spec memakai asumsi seed PB-C1 mereset Changelog company seed ke tepat 9 entri (seed terisolasi menurut Catatan TC); bila reset tidak tersedia, Expected perlu ditulis ulang relatif atau dibatasi Filter Date pada tanggal seed.
  - TC-FA-PREF-300 langkah 2 sampai 7 menulis kata kunci sebagai "kata kunci huruf besar kolom X" tanpa nilai; nilai diambil dari baris Data Uji TC.
  - TC-FA-PREF-301 Expected a dan b adalah dua klausa dengan makna tumpang tindih (empty state dan tidak ada baris Date 26/10/26); spec menulis keduanya sebagai dua `Verifikasi`.
