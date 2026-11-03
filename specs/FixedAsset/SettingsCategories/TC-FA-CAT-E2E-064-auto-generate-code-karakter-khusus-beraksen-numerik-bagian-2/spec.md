---
id: TC-FA-CAT-E2E-064-auto-generate-code-karakter-khusus-beraksen-numerik-bagian-2
title: "Auto-generate Code: Nama Numerik Murni dan Pemotongan 15 Karakter (Bagian 2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-153
  - TC-FA-CAT-154
coverage:
  web: automated
---

# Auto-generate Code: Nama Numerik Murni dan Pemotongan 15 Karakter (Bagian 2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; tidak ada baris seed yang diubah.
- Data yang dibuat spec lewat UI (Category Name literal tanpa suffix karena Code hasil generate diturunkan dari nama itu; ini pengecualian nama literal atas S-12, dan suite berjalan serial). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | TC | Category Name | Code hasil generate yang diharapkan |
  |---|---|---|
  | TC-153 | `2024 25` | `202425` |
  | TC-154 | `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` (16 token) | `ABCDEFGHIJKLMNO` (16 inisial dipotong ke 15 karakter) |

- Hook `before` menghapus sisa kategori ber-Name atau ber-Code di atas dari run lain atau spec lain agar dedup tidak mengubah hasil generate (R-13); hook `after` menghapus kedua kategori yang dibuat spec (disediakan tim FE).
- Kemampuan teknis: pembacaan kolom Code pada tabel Categories List.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-153: Auto-generate Code: nama yang seluruh tokennya numerik murni

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `2024 25` dan biarkan Code kosong
3. Klik `[Submit]`
4. Verifikasi toast `Success, category has been created.`
5. Ketik Search `2024 25`, tekan Enter
6. Verifikasi baris `2024 25` tampil di tabel (kategori tersimpan)
7. Verifikasi kolom Code baris `2024 25` berisi `202425` (dua token numerik passthrough utuh)
8. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
9. Klik `(←)` pada kotak Search

### TC-FA-CAT-154: Auto-generate Code: kandidat dipotong ke batas 15 karakter

10. Klik `[+] Category` pada sidebar
11. Isi Category Name `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` dan biarkan Code kosong
12. Klik `[Submit]`
13. Verifikasi toast `Success, category has been created.`
14. Ketik Search `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa`, tekan Enter
15. Verifikasi baris `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` tampil di tabel (kategori tersimpan)
16. Verifikasi kolom Code baris `Alpha Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliet Kilo Lima Mike November Oscar Papa` berisi `ABCDEFGHIJKLMNO` (16 token menghasilkan 16 inisial dan dipotong ke 15 karakter)
17. Verifikasi Code hasil generate lolos whitelist (huruf kapital, angka, `-`, `_`, `.`) tanpa error V-07 ke user
18. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-153 dan TC-154 ada di spec ini; TC-150, TC-151, dan TC-152 ada di spec 063.
- Nama literal tanpa suffix (S-12, pengecualian khusus): Code diturunkan dari Category Name, sehingga suffix `{runId}` akan mengubah Code yang diuji. Syaratnya dipenuhi lewat Prerequisites.
- Code `ABCDEFGHIJKLMNO` pada client CatMain bebas; pada client CatCode kode yang sama dipakai seed `Panjang 15` (spec 067) dan tidak bentrok karena client berbeda.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): Search untuk menemukan baris hasil (R-16) dan mengosongkan Search lewat `(←)` sebelum TC berikutnya (S-09).
- Temuan untuk QA:
  - TC-153 dan TC-154 Post Condition (Changelog menulis satu baris Create Field `Category Name`; Code hasil generate tidak menulis baris tersendiri) tanpa langkah observasi di TC sehingga tidak diasersi (S-01).
  - Kedua TC menyatakan "kategori tersimpan" pada Expected a tanpa menyebut cara memeriksanya; spec memeriksa kemunculan baris di tabel.
  - TC-154 memakai nama 97 karakter; batas panjang Category Name (V-02, 120 karakter) tidak dilampaui.
