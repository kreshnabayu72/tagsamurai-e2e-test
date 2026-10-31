---
id: TC-GS-GSET-E2E-022-state-tenant-baca-saat-suspended
title: "State Tenant: Halaman General Settings Tetap Dapat Dibaca saat Entitas Suspended"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-56
coverage:
  web: automated
---

# State Tenant: Halaman General Settings Tetap Dapat Dibaca saat Entitas Suspended

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control staff `Client Suspended` (Pre-setup No 16, berstatus Suspended). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; kredensial `Spectra.env.GS_SUSPENDED_TC_PASSWORD` (nama variabel baru, pola `<APP>_<ROLE>_PASSWORD`, belum terdaftar di `spectra.config.ts` dan `.env.example`). Akun default suite adalah Total Control Client A (Budi Santoso, Pre-setup No 1, `Spectra.env.GS_TC_PASSWORD`); hook `after` spec ini mengembalikan sesi ke akun default suite.
- Environment variable: `GS_SUSPENDED_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun aktor tiap spec, termasuk akun staff `Client Suspended`; spec ini tidak mengatur flag sendiri.
- State tenant: status `Client Suspended` sudah berlaku di environment automation dan disediakan tim FE (pelaku perubahan status tidak ada di TC). Spec ini hanya membaca; status entitas dan record tidak diubah, tidak ada state global yang diubah. Record General Settings `Client Suspended` berada pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), disediakan tim FE.
- Halaman awal: Global Settings (precondition b TC), bukan General Settings; membuka General Settings adalah langkah 1 spec ini (objek uji).
- TC-GS-GSET-56: login sebagai Total Control staff `Client Suspended` dan berada di Global Settings.

## Test Steps

### TC-GS-GSET-56: Pembacaan tetap berjalan saat Suspended

1. Buka Global Settings > General Settings lewat menu pada sidebar
2. Verifikasi form terisi nilai tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
3. Verifikasi tidak ada error
4. Verifikasi tidak ada banner atau perlakuan UI khusus

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Kelas state tenant (prinsip 13h): verifikasi baca murni dipisah dari write-lockdown (spec 021).
- Pemetaan Expected: TC-GS-GSET-56 ke langkah 2 (form terisi nilai tersimpan), 3 (tanpa error), dan 4 (tanpa banner atau perlakuan UI khusus).
- Langkah 2 membaca lima field sekaligus sebagai satu daftar elemen yang disebut utuh ("nilai tersimpan" menurut precondition record baseline).
- Spec ini tidak membuat langkah penghubung.
- Temuan untuk QA:
  - TC-GS-GSET-56: email akun staff `Client Suspended` tidak ada di Tabel Data Uji Pre-setup (hanya entitas No 16); akun dan keadaan status entitas disediakan tim FE.
  - TC-GS-GSET-56: TC tidak menyebut record General Settings `Client Suspended` yang tersimpan; spec mengasumsikan baseline Pre-setup No 10 (precondition c tidak ada di TC ini).
