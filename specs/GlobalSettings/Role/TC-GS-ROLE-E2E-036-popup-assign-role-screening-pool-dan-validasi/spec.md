---
id: TC-GS-ROLE-E2E-036-popup-assign-role-screening-pool-dan-validasi
title: "Popup Assign Role: Screening, Pool, dan Validasi Tanpa Memilih User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-92
  - TC-GS-ROLE-93
coverage:
  web: automated
---

# Popup Assign Role: Screening, Pool, dan Validasi Tanpa Memilih User

## Prerequisites

- Mode: FE+BE.
- Akun aktor (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Spec tidak berganti akun.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab System > Detail "Manage TAG".
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (hanya dibaca, tidak ada aksi tulis, sehingga tanpa suffix `+{runId}-036` dan tanpa pemulihan):
  - Sudah punya baris Manage TAG: Doni Pratama (Pre-setup #10), Budi Santoso (Pre-setup #2), Siti Nurhaliza (Pre-setup #4).
  - Belum punya baris Manage TAG: Wawan Setiawan (Pre-setup #11), Agus Salim (Pre-setup #9, Access Global Settings dicentang), Tari Anjani (Inactive) dan Yoga Pratama (Pending Activation) (Pre-setup #18, tanpa baris role).
  - Ahmad Fauzi (Pre-setup #1) adalah aktor.
- Kemampuan teknis: tidak ada tambahan di luar login UI.

Tabel Pool, nama yang dicari di picker Assign Role Detail "Manage TAG" (TC-GS-ROLE-92):

| Nama | Hasil yang diharapkan |
|---|---|
| Wawan Setiawan | baris tampil |
| Agus Salim | baris tampil |
| Tari Anjani | baris tampil |
| Yoga Pratama | baris tampil |
| Doni Pratama | `No results found` tampil |
| Budi Santoso | `No results found` tampil |
| Siti Nurhaliza | `No results found` tampil |
| Ahmad Fauzi | `No results found` tampil |

## Test Steps

### TC-GS-ROLE-92: Screening Popup Assign Role dan pool-nya

1. Klik `[+ Assign]`
2. Verifikasi Title popup `Assign Role` tampil
3. Verifikasi toolbar `Search | Filter` tampil
4. Verifikasi kolom tabel picker `Checkbox | Name | Email | Position | Division | Status`
5. Verifikasi footer `[Cancel] | [Assign]` tampil

Untuk setiap baris Tabel Pool (langkah 6 sampai 7):

6. Ketik Search `<nama>`, tekan Enter
7. Verifikasi hasil pada kolom "Hasil yang diharapkan" tampil

8. Klik `(←)` pada kotak Search

### TC-GS-ROLE-93: Submit Assign Role tanpa memilih user

9. Klik `[Assign]`
10. Verifikasi teks error inline `You must pick a user` (danger) tampil di atas tombol footer
11. Verifikasi popup `Assign Role` tetap terbuka
12. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 TC-GS-ROLE-93 ("Klik [+ Assign]") dipenuhi oleh popup yang sama dengan TC-GS-ROLE-92 (tidak dibuka ulang; Search dibersihkan pada langkah 8); satu popup dibuka untuk screening dan validasi kosong, ditutup di langkah 12 (bagian 3 prinsip 6 dan 8).
- Tabel Pool memuat baris tampil lebih dahulu sebagai anchor positif sebelum baris `No results found` (bagian 8b butir 2); `No results found` pada hasil pencarian satu nama adalah anchor sah bagi absence nama itu di pool. Urutan Expected TC-GS-ROLE-92 (b tidak tampil, c tampil) dibalik untuk alasan ini. Jumlah langkah 12 nominal, sekitar 19 dengan ekspansi perulangan langkah 6 sampai 7 untuk delapan baris Tabel Pool.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik `(←)` pada kotak Search (langkah 8) dan klik `[Cancel]` menutup popup (langkah 12).
- Langkah 11 (popup tetap terbuka) didahului teks error inline pada langkah 10 sebagai anchor positif bahwa klik `[Assign]` sudah diproses.
- Temuan untuk QA:
  - TC-GS-ROLE-92 Expected c menyebut status Tari Anjani (Inactive) dan Yoga Pratama (Pending Activation) dalam tanda kurung tanpa menyatakan apakah badge atau Status harus diasersi; spec hanya mengasersi barisnya tampil.
  - Expected TC-GS-ROLE-92 b menyebut "Ahmad Fauzi (aktor)" tidak tampil; spec mencarinya dengan Search `Ahmad Fauzi` (tidak bentrok dengan Ahmad Fauzan Pre-setup #11).
