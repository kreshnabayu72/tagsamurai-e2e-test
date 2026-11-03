---
id: TC-FA-GRP-E2E-162-tab-users-search-per-kolom-name-email-position-dan-division
title: "Tab Users Search per Kolom Name, Email, Position, dan Division"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-573
  - TC-FA-GRP-574
  - TC-FA-GRP-575
  - TC-FA-GRP-576
coverage:
  web: automated
---

# Tab Users Search per Kolom Name, Email, Position, dan Division

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): potongan nilai tiap kolom pada tabel iterasi di bawah; masing-masing mencocokkan sedikitnya satu baris dan tidak semua baris.

  | Kolom | Potongan nilai (huruf kecil) | Potongan sama (KAPITAL) | String tanpa match |
  |---|---|---|---|
  | Name | `Fixture.groupsTabUsers.nameKeyword` (huruf kecil) | `Fixture.groupsTabUsers.nameKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |
  | Email | `Fixture.groupsTabUsers.emailKeyword` (huruf kecil) | `Fixture.groupsTabUsers.emailKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |
  | Position | `Fixture.groupsTabUsers.positionKeyword` (huruf kecil) | `Fixture.groupsTabUsers.positionKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |
  | Division | `Fixture.groupsTabUsers.divisionKeyword` (huruf kecil) | `Fixture.groupsTabUsers.divisionKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 10): Pastikan kolom pada baris tabel tampil
3. Ketik Search potongan huruf kecil dari tabel, tekan Enter
4. Verifikasi sedikitnya satu baris tampil dan baris yang nilai kolom tersebut mengandung substring tampil
5. Verifikasi baris yang nilai kolom tersebut tidak mengandung substring tidak tampil
6. Ganti isi kotak search dengan potongan KAPITAL dari tabel, tekan Enter
7. Verifikasi baris yang tampil identik dengan hasil huruf kecil (case-insensitive)
8. Ganti isi kotak search dengan string tanpa match dari tabel, tekan Enter
9. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter."
10. Klik `✕` pada Search, tekan Enter

## Notes

- Langkah 2 sampai 10 berulang untuk setiap baris tabel Prerequisites (Name, Email, Position, Division); satu `Verifikasi` per klausa tetap dipertahankan (8b butir 7). Langkah terakhir iterasi (klik `✕` pada Search, tekan Enter) adalah langkah penghubung yang mengosongkan Search sebelum iterasi berikut (S-03, S-09).
- Spec memiliki 10 langkah nominal dan 37 langkah setelah ekspansi (4 iterasi x 9 langkah + 1), di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (Search Tab Users pada dataset yang sama), langkah tiap kolom identik sehingga ekspansi berasal dari perulangan per kolom tanpa langkah bersyarat (8b butir 7).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-573 menulis "pencocokan terhadap teks Full Name saja; avatar tidak dicari"; klausa "avatar tidak dicari" tidak punya cara amati terpisah dan dicakup oleh asersi "baris lain tidak tampil".
  - Potongan nilai tiap kolom "dari Tabel Data Uji" tidak punya tabel konkret; spec memakai fixture baru `Fixture.groupsTabUsers.*` yang ditetapkan tim FE.
