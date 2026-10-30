---
id: TC-GS-ROLE-E2E-107-realtime-auto-revert-pada-tab-total-control-sesi-admin-lain
title: "Realtime: Auto-Revert Menghilangkan User dari Tab Total Control Sesi Admin Lain Tanpa Reload"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-277
coverage:
  web: automated
---

# Realtime: Auto-Revert Menghilangkan User dari Tab Total Control Sesi Admin Lain Tanpa Reload

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua sesi UI admin), kelas c. Suite `parallel: false`.
- Akun Sesi A (UI): Ahmad Fauzi (Total Control, akun hook `before`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (UI kedua, objek asersi): Eko Prasetyo (Total Control kedua, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Sesi B dibuka sebagai konteks browser kedua dengan sesi login sendiri di hook `before`; hook `after` menutup konteks Sesi B dan menghapus sesi login terkaitnya. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser paralel (Sesi A dan Sesi B) yang dikendalikan dalam satu spec; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`; pembaruan realtime (SSE) tiba di Sesi B tanpa reload.
- Data Pre-setup #18: `Indra Gunawan` (Active, Access Global Settings dicentang, tanpa baris role) dengan Given Total Control di-assign lewat sesi API Ahmad Fauzi di hook `before`. Hook `after` mencabut Total Control dan menghapus baris role `Indra Gunawan` bila masih ada sehingga kembali ke Pre-setup #18.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun Sesi A dan Sesi B; spec ini tidak mengatur flag sendiri.
- Layar awal Sesi A (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-277: Auto-revert menghilangkan user dari Tab Total Control sesi admin lain secara realtime

1. [Sesi B] Buka Tab `Total Control`
2. [Sesi B] Verifikasi baris `Indra Gunawan` tampil di Tab Total Control
3. [Sesi A] Buka Detail "Manage TAG"
4. [Sesi A] Hapus centang Update pada baris `Indra Gunawan`
5. [Sesi A] Klik `[Remove]` pada dialog `Remove Access`
6. [Sesi A] Tunggu aksi selesai (dialog tertutup)
7. [Sesi B] Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control tanpa memuat ulang
8. [Sesi B] Verifikasi baris `Indra Gunawan` tidak ada di Tab Total Control tanpa memuat ulang

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua sesi UI), prinsip 13c bagian 3 konvensi. Sesi B adalah konteks browser kedua yang menjadi objek asersi (bukan pemicu), sehingga butir `P-2` tidak dipakai.
- Langkah penghubung (aksi tanpa `Verifikasi`): menunggu aksi selesai sebelum berpindah sesi (langkah 6).
- Langkah 2 (Given terlihat di Sesi B) adalah asersi tambahan yang tidak ada di Expected TC; ia memastikan sesi B sudah merender `Indra Gunawan` sebelum auto-revert. Langkah 7 adalah baris pembanding sebelum absence `Indra Gunawan` di langkah 8 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-277 Langkah 1 menulis "auto-revert Indra Gunawan lewat Edit CRUD > [Remove]" tanpa menyebut Detail role dan cell yang diedit; spec memakai Detail "Manage TAG" dan menghapus centang Update pada baris `Indra Gunawan` (pola TC-GS-ROLE-106), lalu `[Remove]` pada dialog `Remove Access`.
  - TC-277 tidak menyebut batas waktu pembaruan realtime; asersi memakai penantian bawaan framework.
  - TC-277 Expected tidak menyebut toast Sesi A; tidak diasersi.
