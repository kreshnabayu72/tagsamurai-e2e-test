---
id: TC-AC-ACC-E2E-241-search-station-list-kolom-teks-dan-numerik
title: "Search Station List: Kolom Teks (Reader Name, Reader Group, Reader ID, Reader Model, Status) dan Kolom Numerik (Ports)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-311
  - TC-AC-ACC-789
coverage:
  web: automated
---

# Search Station List: Kolom Teks (Reader Name, Reader Group, Reader ID, Reader Model, Status) dan Kolom Numerik (Ports)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca, tidak diubah): Client C-01 "PT Sejahtera Abadi" dengan Station List: "Gerbang Gudang A" (Active, Reader Group (Fixed Asset) "Gudang Pusat", Reader Group (Supply) kosong, Reader ID RDR-0001, Reader Model SFR-100, Ports 4); "Gerbang Gudang B" (Inactive, "Gudang Pusat", "Supply Utama", RDR-0002, SFR-100, Ports 4); "Gerbang Lama" (Deactivated, kedua group kosong, RDR-0003, SFR-100, Ports 2). Seluruh kolom Station List dalam keadaan default (Visible); Search terikat visibilitas kolom.
- Kolom Station List yang diuji Search (parameter blok langkah 3 sampai 6):

| Kolom | Kata kunci | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Reader Name | gudang b | Gerbang Gudang B | Gerbang Gudang A, Gerbang Lama |
| Reader Group (Fixed Asset) | gudang pusat | Gerbang Gudang A, Gerbang Gudang B | Gerbang Lama |
| Reader Group (Supply) | supply utama | Gerbang Gudang B | Gerbang Gudang A, Gerbang Lama |
| Reader ID | rdr-0003 | Gerbang Lama | Gerbang Gudang A, Gerbang Gudang B |
| Status | deactivated | Gerbang Lama | Gerbang Gudang A, Gerbang Gudang B |

- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control

### TC-AC-ACC-311: Search Station List kolom teks

2. Klik ikon Search pada toolbar Station List
3. Untuk setiap baris tabel "Kolom Station List yang diuji Search": ketik kata kunci pada kolom Search, tekan Enter (langkah 3 sampai 6)
4. Verifikasi baris pada kolom "Baris tampil" tampil
5. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
6. Klik ikon ✕ pada input Search lalu tekan Enter
7. Ketik Search "sfr-100", tekan Enter
8. Verifikasi Gerbang Gudang A, Gerbang Gudang B, dan Gerbang Lama tampil
9. Klik ikon ✕ pada input Search lalu tekan Enter

### TC-AC-ACC-789: Search Station List kolom numerik Ports

10. Ketik Search "4", tekan Enter
11. Verifikasi Gerbang Gudang A dan Gerbang Gudang B (Ports 4) tampil
12. Verifikasi Gerbang Lama (Ports 2) tidak tampil
13. Klik ikon ✕ pada input Search lalu tekan Enter

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 6, 9, 13 (mengosongkan Search dan mereset tabel sebelum kata kunci berikutnya, S-09).
- Langkah 3 sampai 6 diulang untuk 5 baris tabel (20 langkah setelah ekspansi); Reader Model (langkah 7 sampai 9) ditulis eksplisit karena tidak punya baris yang tidak tampil sehingga tidak masuk blok berulang. Urutan kata kunci (Reader Model sesudah Status) berbeda dari urutan Data Uji TC; urutan kata kunci tidak bermakna asal Search dikosongkan sebelum tiap kata kunci.
- Temuan untuk QA:
  - TC-AC-ACC-311 dan TC-AC-ACC-789 tidak menyebut nilai Reader Model dan Ports Pre-setup secara eksplisit selain di Expected (SFR-100 untuk ketiga baris; Ports 4, 4, 2); spec mengikuti Expected.
