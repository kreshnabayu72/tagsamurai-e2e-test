---
id: TC-GS-GSET-E2E-021-state-tenant-save-ditolak-suspended-dan-expired
title: "State Tenant: Save Ditolak saat Entitas Suspended dan Expired"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-54
  - TC-GS-GSET-55
coverage:
  web: automated
---

# State Tenant: Save Ditolak saat Entitas Suspended dan Expired

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (dua entitas, Step ganti akun eksplisit di langkah 9 dan 10):

  | Peran dalam spec | Role | Entitas | Email | Environment variable password |
  |---|---|---|---|---|
  | Aktor langkah 1 sampai 8 | Total Control staff `Client Suspended` | `Client Suspended` (Pre-setup No 16, berstatus Suspended) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `GS_SUSPENDED_TC_PASSWORD` |
  | Aktor langkah 10 sampai 17 | Total Control staff `Client Expired` | `Client Expired` (Pre-setup No 17, berstatus Expired) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `GS_EXPIRED_TC_PASSWORD` |

  Login akun pertama (staff `Client Suspended`) di hook `before` spec ini. Akun default suite adalah Total Control Client A (Budi Santoso, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.GS_TC_PASSWORD`); hook `after` spec ini mengembalikan sesi ke akun default suite. Halaman awal: Global Settings > General Settings.
- Environment variable: `GS_SUSPENDED_TC_PASSWORD`, `GS_EXPIRED_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama variabel baru mengikuti pola `<APP>_<ROLE>_PASSWORD` dan belum terdaftar di `spectra.config.ts` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun aktor tiap spec, termasuk dua akun staff di atas; spec ini tidak mengatur flag sendiri.
- State tenant: status `Client Suspended` dan `Client Expired` sudah berlaku di environment automation dan disediakan tim FE (pelaku perubahan status tidak ada di TC). Spec ini tidak mengubah status entitas dan tidak mengubah state global; Save ditolak sehingga record kedua entitas tidak berubah. Record General Settings kedua entitas berada pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), disediakan tim FE.
- Kemampuan teknis: (a) membaca status respons PUT `/v2/enterprise-management/general-settings` yang dipicu UI (`403`); (b) memuat ulang halaman dengan konfirmasi bawaan browser `beforeunload` dikonfirmasi otomatis oleh harness (form masih berisi perubahan belum tersimpan), tanpa langkah bersyarat.
- Data Uji: Session Idle Timeout `1 hour` (TC-GS-GSET-54), Time Format `hh:mm a` (TC-GS-GSET-55). Tidak ada Data Dinamis dan tidak ada baris Changelog yang dihasilkan.
- TC-GS-GSET-54 dan 55: login sebagai Total Control staff entitas yang bersangkutan dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-54: Save ditolak saat entitas Suspended

1. Pilih Session Idle Timeout `1 hour`
2. Klik `[Save]`
3. Verifikasi server menolak dengan `403 Forbidden`
4. Verifikasi toast: `Changes can't be saved while this workspace is suspended or expired.`
5. Verifikasi form tetap unsaved dengan Session Idle Timeout `1 hour`
6. Verifikasi field dan Button "Save" tidak diberi perlakuan UI khusus
7. Muat ulang halaman (F5), konfirmasi bawaan browser `beforeunload` dikonfirmasi
8. Verifikasi pembacaan tetap berjalan: Session Idle Timeout `30 minutes` (tidak tersimpan)

### Ganti akun ke staff Client Expired

9. Logout dari akun Total Control staff `Client Suspended`
10. Login sebagai Total Control staff `Client Expired` (`Spectra.env.GS_EXPIRED_TC_PASSWORD`) lalu buka Global Settings > General Settings

### TC-GS-GSET-55: Save ditolak saat entitas Expired

11. Pilih Time Format `hh:mm a`
12. Klik `[Save]`
13. Verifikasi server menolak dengan `403 Forbidden`
14. Verifikasi toast: `Changes can't be saved while this workspace is suspended or expired.`
15. Verifikasi form tetap unsaved dengan Time Format `hh:mm a`
16. Muat ulang halaman (F5), konfirmasi bawaan browser `beforeunload` dikonfirmasi
17. Verifikasi pembacaan tetap berjalan: Time Format `HH:mm` (tidak tersimpan)

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Kelas state tenant (prinsip 13h): write-lockdown Suspended dan Expired. Verifikasi baca murni saat Suspended ada di spec 022.
- Dua akun dalam satu spec sah (konvensi bagian 3, pemisah "beda akun"): ada Step ganti akun eksplisit (langkah 9 dan 10) dan blok sesudahnya tetap bermakna walau blok sebelumnya gagal; spec tidak mencampur kelas harness.
- Pemetaan Expected: TC-GS-GSET-54 a ke langkah 3 dan 4, b ke 5 dan 6, c ke 8; TC-GS-GSET-55 a ke langkah 13 dan 14, b ke 15, c ke 17.
- Langkah 10 menggabungkan login dan pembukaan halaman karena sesi baru belum berada di General Settings.
- Langkah penghubung: langkah 7 dan 16 (muat ulang halaman, memuat ulang pembacaan nilai tersimpan sesuai langkah 3 TC-GS-GSET-54 dan 55).
- Temuan untuk QA:
  - TC-GS-GSET-54 dan 55: email akun staff `Client Suspended` dan `Client Expired` tidak ada di Tabel Data Uji Pre-setup (hanya entitas No 16 dan 17); akun dan keadaan status entitas disediakan tim FE.
  - TC-GS-GSET-54 dan 55: TC tidak menyebut pelaku perubahan status entitas (Suspended atau Expired), sehingga spec memakai entitas yang sudah berstatus demikian di environment.
  - TC-GS-GSET-54: langkah 3 TC memuat ulang halaman saat form berisi perubahan belum tersimpan, sehingga browser menampilkan konfirmasi bawaan `beforeunload` (PC §24.1d); TC tidak menyebutnya (juga pada TC-GS-GSET-55).
