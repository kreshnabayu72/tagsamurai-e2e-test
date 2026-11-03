---
id: TC-FA-GRP-E2E-163-tab-users-search-per-kolom-activation-status-temporary-user-tag-dan-custom-field
title: "Tab Users Search per Kolom Activation Status, Temporary User, TAG, dan Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-579
  - TC-FA-GRP-580
  - TC-FA-GRP-581
  - TC-FA-GRP-582
coverage:
  web: automated
---

# Tab Users Search per Kolom Activation Status, Temporary User, TAG, dan Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Kolom Activation Status, Temporary User, TAG, dan Custom Field aktif Phone adalah kolom curated (tidak tampil default) yang ditampilkan lewat Column Visibility pada tiap iterasi. Pemulihan: hapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): potongan nilai tiap kolom; masing-masing mencocokkan sedikitnya satu baris dan tidak semua baris.

  | Kolom | Potongan nilai (huruf kecil) | Potongan sama (KAPITAL) | String tanpa match |
  |---|---|---|---|
  | Activation Status | `Fixture.groupsTabUsers.activationKeyword` (huruf kecil) | `Fixture.groupsTabUsers.activationKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |
  | Temporary User | `Fixture.groupsTabUsers.tempUserKeyword` (huruf kecil) | `Fixture.groupsTabUsers.tempUserKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |
  | TAG | `Fixture.groupsTabUsers.tagKeyword` (huruf kecil) | `Fixture.groupsTabUsers.tagKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |
  | Custom Field Phone | `Fixture.groupsTabUsers.phoneKeyword` (huruf kecil) | `Fixture.groupsTabUsers.phoneKeyword` diubah ke KAPITAL | `Fixture.groupsTabUsers.noMatch` |

## Test Steps

1. Klik angka Total User Warehouse A
2. Untuk setiap baris tabel Prerequisites (langkah 2 sampai 10): Tampilkan kolom pada baris tabel via Column Visibility
3. Ketik Search potongan huruf kecil dari tabel, tekan Enter
4. Verifikasi sedikitnya satu baris tampil dan baris yang nilai kolom tersebut mengandung substring tampil
5. Verifikasi baris yang nilai kolom tersebut tidak mengandung substring tidak tampil
6. Ganti isi kotak search dengan potongan KAPITAL dari tabel, tekan Enter
7. Verifikasi baris yang tampil identik dengan hasil huruf kecil (case-insensitive)
8. Ganti isi kotak search dengan string tanpa match dari tabel, tekan Enter
9. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter."
10. Klik `✕` pada Search, tekan Enter

## Notes

- Langkah 2 sampai 10 berulang untuk setiap baris tabel Prerequisites; langkah terakhir iterasi (klik `✕` pada Search, tekan Enter) adalah langkah penghubung yang mengosongkan Search sebelum iterasi berikut (S-03, S-09). Kolom curated tetap tampil sampai hook `after`.
- Spec memiliki 10 langkah nominal dan 37 langkah setelah ekspansi (4 iterasi x 9 langkah + 1), di atas smell 35 langkah. Alasan: seluruh blok satu topik (Search Tab Users pada dataset yang sama) dan langkah tiap kolom identik, sehingga ekspansi berasal dari perulangan per kolom tanpa langkah bersyarat (8b butir 7).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - Potongan nilai tiap kolom "dari Tabel Data Uji" tidak punya tabel konkret; spec memakai fixture baru `Fixture.groupsTabUsers.*` yang ditetapkan tim FE.
  - TC-581 mengasumsikan kolom TAG punya nilai pada sedikitnya satu user Warehouse A; Pre-setup tidak menyebut data TAG user.
