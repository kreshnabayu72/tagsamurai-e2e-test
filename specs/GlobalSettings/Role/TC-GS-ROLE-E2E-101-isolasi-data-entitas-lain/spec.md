---
id: TC-GS-ROLE-E2E-101-isolasi-data-entitas-lain
title: "Isolasi Data: Permintaan List Tab Total Control dengan Identitas Client Lain Tidak Mengembalikan User Client Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-262
coverage:
  web: automated
---

# Isolasi Data: Permintaan List Tab Total Control dengan Identitas Client Lain Tidak Mengembalikan User Client Lain

## Prerequisites

- Mode: FE+BE. Kelas harness: defense-in-depth (request langsung ke server, isolasi data antar-entitas), kelas a. Suite `parallel: false`.
- Akun aktor: Ahmad Fauzi (Total Control Client A), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi Ahmad Fauzi (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi respons hanya isi respons server; tampilan Tab Total Control diasersi sebagai state data yang dirender dari server.
- Data Client B (Pre-setup #14): identitas Client B (parameter atau identitas yang dikirim pada permintaan) dan identitas user Total Control Client B (Default User Client B) disediakan tim FE. Spec tidak login ke Client B sehingga password Client B (`GS_CLIENTB_TC_PASSWORD`) tidak dipakai.
- Spec tidak mengubah data; tidak ada seeding atau pemulihan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-262: Data Role & Permission client lain tidak dapat dibaca

1. Kirim permintaan langsung list Tab Total Control dengan parameter atau identitas Client B dengan sesi Ahmad Fauzi
2. Verifikasi respons permintaan tidak mengembalikan user Client B
3. Klik Tab `Total Control`
4. Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control
5. Verifikasi Tab Total Control tidak memuat user Total Control Client B

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: defense-in-depth (a), prinsip 13a bagian 3 konvensi.
- Expected b ("Tab Total Control hanya memuat user Client A") dipecah menjadi langkah 4 (baris Client A tampil, sekaligus anchor positif) dan langkah 5 (user Client B tidak ada), sesuai bagian 8b butir 2.
- Permintaan langsung hanya diasersi pada isi respons server (bagian 8b butir 1); langkah 2 TC ("Amati Tab Total Control Client A") ditulis sebagai langkah 3 sampai 5.
- Temuan untuk QA:
  - TC-262 menyebut "parameter/identitas Client B" tanpa menyebut parameter atau endpoint; `global-settings/role/API/openapi.yaml` hanya memuat path dengan `{product}` dan tidak memuat parameter Client. Cara mengirim identitas Client B disediakan tim FE.
  - TC-262 Expected a tidak menyebut status respons (kosong, 403, atau daftar Client A); spec hanya mengasersi bahwa user Client B tidak dikembalikan.
  - Identitas user Total Control Client B tidak ada di Tabel Pre-setup selain deskripsi #14 (hanya Default User sebagai Total Control); disediakan tim FE.
