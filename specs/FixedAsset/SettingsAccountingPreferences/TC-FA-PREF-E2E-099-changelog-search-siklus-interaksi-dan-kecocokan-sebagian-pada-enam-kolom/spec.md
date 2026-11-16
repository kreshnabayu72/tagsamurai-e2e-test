---
id: TC-FA-PREF-E2E-099-changelog-search-siklus-interaksi-dan-kecocokan-sebagian-pada-enam-kolom
title: "Changelog Search: Siklus Interaksi, Kecocokan Sebagian pada Enam Kolom Searchable"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-298
  - TC-FA-PREF-299
sourceRules: ["§4.1.4#b1", "§4.1.4#p2", "§4.1.4#r4", "§4.1.4#r2", "§4.1.4#r3", "§4.1.4#r5", "§4.1.4#r6", "§4.1.4#r7"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#b1": 4
  "§4.1.4#p2": [7, 15, 19]
  "§4.1.4#r4": [9, 13, 21]
  "§4.1.4#r2": 21
  "§4.1.4#r3": 21
  "§4.1.4#r5": 21
  "§4.1.4#r6": 21
  "§4.1.4#r7": 21
anchor: [3, 6, 11, 12, 18]
coverage:
  web: automated
---

# Changelog Search: Siklus Interaksi, Kecocokan Sebagian pada Enam Kolom Searchable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PB-1; Changelog Preferences berisi 9 entri contoh PB-C1 (format tanggal dd/MM/yy dan 24 jam). Posisi baris pada urutan default Date Newest First (sama dengan TC-FA-PREF-290): baris 1 Edit Chart of Accounts Default Capitalization Offset (Budi S); baris 2 Edit Disposal Disposal Documents — Sell, Optional ke Required (Rina A); baris 3 Edit Disposal Disposal Documents — Scrap, Optional ke Required (Rina A); baris 4 Edit Journal Export Journal Grouping, Group ke Group, Category (Budi S); baris 5 Edit Disposal Default Gain on Disposal (Rina A); baris 6 Edit General Fiscal Year Start, January ke April (Rina A); baris 7 Edit General First Accounting Period, Mar 2026 ke Jan 2026 (Rina A); baris 8 Edit Capitalization Default Capitalization Threshold (Rina A); baris 9 Create Preferences, Initial values (Budi S). Urutan tulis seed: pada Date yang sama baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed PB-C1 mengatur Changelog company seed ke tepat 9 entri (lihat Temuan untuk QA).
- Tabel "Kata kunci per kolom" (TC-FA-PREF-299; langkah 20 sampai 22 diulang untuk tiap baris tabel):

  | Kolom | Kata kunci | Baris yang tampil, berurutan |
  |---|---|---|
  | Action | Create | baris 9 |
  | Section | Journal Export | baris 4 |
  | Field | Fiscal | baris 6 |
  | Old Value | Mar 2026 | baris 7 |
  | New Value | Required | baris 2, baris 3 |
  | Modified By | Budi | baris 1, baris 4, baris 9 |

- Spec ini tidak menulis ke Changelog; Search dan Filter tidak mengubah state server.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-298: Siklus interaksi Search: reveal, Enter, clear, dan collapse

1. Klik ikon View history di header tab Preferences
2. Klik ikon Search pada toolbar modal
3. Verifikasi kotak pencarian melebar dengan kursor fokus di dalam input
4. Verifikasi placeholder "Search changelog..." tampil
5. Ketik "Fiscal" tanpa menekan Enter
6. Verifikasi ikon (✕) muncul di dalam input
7. Verifikasi tabel masih menampilkan 9 baris
8. Tekan Enter
9. Verifikasi tabel menampilkan hanya baris 6 (Field Fiscal Year Start)
10. Klik ikon (✕) di dalam kotak pencarian
11. Verifikasi teks input kosong
12. Verifikasi kotak pencarian tetap terbuka
13. Verifikasi tabel masih menampilkan hanya baris 6
14. Tekan Enter pada input kosong
15. Verifikasi tabel kembali menampilkan 9 baris
16. Ketik Search "Fiscal", tekan Enter
17. Klik ikon panah (←) di kiri toolbar
18. Verifikasi kotak pencarian menutup kembali menjadi ikon Search
19. Verifikasi tabel langsung kembali menampilkan 9 baris

### TC-FA-PREF-299: Search mencocokkan sebagian teks pada enam kolom searchable

20. Untuk setiap baris tabel "Kata kunci per kolom" (langkah 20 sampai 22): ketik Search kata kunci kolom itu, tekan Enter
21. Verifikasi tabel menampilkan baris yang tertera pada kolom "Baris yang tampil, berurutan" tabel itu
22. Kosongkan isi kotak search, tekan Enter
23. Klik ikon [✕] di header modal Changelog

## Notes

- Langkah penghubung (S-03, S-09): langkah 10 sampai 15 dan 17 mengikuti Expected TC-FA-PREF-298; langkah 16 mengetik ulang kata kunci sebelum kotak ditutup lewat (←) (langkah TC 7). Langkah 22 (mengosongkan Search dan menyetel ulang tabel) adalah bagian dari langkah TC-FA-PREF-299 dan menjadi langkah pemulihan sebelum kata kunci berikutnya (S-09). Langkah 23 menutup modal.
- Langkah 20 sampai 22 diulang untuk enam baris tabel Prerequisites (bagian 8b butir 7); `Verifikasi` tetap satu per klausa Expected (S-01): satu `Verifikasi` per kata kunci. Dengan ekspansi spec ini 38 langkah; kedua blok berdiri sendiri, memakai satu modal dan dataset yang sama, dan blok 299 adalah satu siklus berpola (parameter tiap iterasi ada di tabel) sehingga tidak dipecah.
- Asersi "hanya baris N" (langkah 9, 13, 21) didahului asersi 9 baris pada langkah 7 dan 15 sebagai pembanding bahwa tabel sudah termuat (bagian 8b butir 2).
- Pencarian ditulis mengikuti bagian 8b butir 9: Search hanya menyaring saat Enter; kotak sudah terbuka pada iterasi berikutnya dan isinya dikosongkan langkah 22.
- Temuan untuk QA:
  - TC-FA-PREF-298 dan 299 mengasersi posisi dan jumlah baris seed ("baris 6", "9 baris") yang bergantung pada Changelog tepat 9 entri seed; Changelog adalah audit trail permanen yang tumbuh karena Save pada spec lain (S-12, S-14). Spec memakai asumsi seed PB-C1 mereset Changelog company seed ke tepat 9 entri (seed terisolasi menurut Catatan TC); bila reset tidak tersedia, Expected perlu ditulis ulang relatif atau dibatasi Filter Date pada tanggal seed.
  - TC-FA-PREF-299 langkah 2 sampai 7 menulis kata kunci sebagai "kata kunci kolom X" tanpa nilai; nilai diambil dari baris Data Uji TC.
  - TC-FA-PREF-298 Expected e menyebut Enter pada input kosong mengembalikan 9 baris tanpa menyebut ikon (✕) yang sudah diklik; spec mengikuti urutan langkah TC.
