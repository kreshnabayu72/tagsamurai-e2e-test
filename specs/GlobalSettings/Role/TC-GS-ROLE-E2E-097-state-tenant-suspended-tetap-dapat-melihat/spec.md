---
id: TC-GS-ROLE-E2E-097-state-tenant-suspended-tetap-dapat-melihat
title: "State Tenant Suspended: Tab dan Detail Role & Permission Tetap Dapat Dilihat"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-271
coverage:
  web: automated
---

# State Tenant Suspended: Tab dan Detail Role & Permission Tetap Dapat Dilihat

## Prerequisites

- Mode: FE+BE. Kelas harness: state tenant (h), verifikasi baca pada Client Suspended. Suite `parallel: false`.
- Akun aktor: Total Control pada Client C suspended (Pre-setup #16), email disediakan tim FE, password `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Client C: disediakan tim FE sebelum status Suspended, mengikuti Pre-setup Role (Tab Total Control dan Read Only berisi baris, Detail "Manage TAG" berisi baris). Status Suspended Client C disetel tim FE; spec tidak mengubah status Client maupun data.
- Spec tidak menjalankan aksi tulis; tidak ada Given atau pemulihan data.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-271: Client suspended tetap dapat melihat Role & Permission

1. Klik Tab `Total Control`
2. Verifikasi Tab Total Control termuat normal (tabel dan baris data tampil tanpa pesan error)
3. Klik Tab `Read Only`
4. Verifikasi Tab Read Only termuat normal (tabel dan baris data tampil tanpa pesan error)
5. Klik Tab `System`
6. Verifikasi Tab System termuat normal (daftar role tampil tanpa pesan error)
7. Klik baris `Manage TAG` untuk membuka Detail "Manage TAG"
8. Verifikasi Detail "Manage TAG" termuat normal (tabel dan baris data tampil tanpa pesan error)

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: state tenant (h), prinsip 13h bagian 3 konvensi; verifikasi baca murni dipisah dari spec write-lockdown (`TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level` dan `TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail`).
- Expected TC "Semua tab dan Detail termuat normal" dipecah satu `Verifikasi` per surface (Tab Total Control, Tab Read Only, Tab System, Detail) dan "termuat normal" didefinisikan sebagai tabel atau daftar dengan data tampil tanpa pesan error.
- Temuan untuk QA:
  - TC-271 menulis langkah "Detail" tanpa menyebut role; spec memakai Detail "Manage TAG" (konsisten dengan TC-267 sampai TC-270).
  - TC-271 tidak mendefinisikan "termuat normal"; spec memakai definisi di atas.
