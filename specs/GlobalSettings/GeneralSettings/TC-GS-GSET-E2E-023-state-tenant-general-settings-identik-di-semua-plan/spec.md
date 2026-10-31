---
id: TC-GS-GSET-E2E-023-state-tenant-general-settings-identik-di-semua-plan
title: "State Tenant: General Settings Tersedia dan Identik di Semua Plan Tanpa Gating"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-123
coverage:
  web: automated
---

# State Tenant: General Settings Tersedia dan Identik di Semua Plan Tanpa Gating

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (Total Control staff tiap entitas; ganti akun eksplisit di langkah 8, 16, dan 24):

  | Plan | Entitas (Pre-setup) | Email | Environment variable password | Langkah |
  |---|---|---|---|---|
  | Starter | `Client Starter` (No 20) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `GS_STARTER_TC_PASSWORD` | 1 sampai 7 |
  | Growth | `Client Growth` (No 21) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `GS_GROWTH_TC_PASSWORD` | 8 sampai 15 |
  | Professional | `Client Professional` (No 22) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `GS_PROFESSIONAL_TC_PASSWORD` | 16 sampai 23 |
  | Enterprise | `Client Enterprise` (No 23) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `GS_ENTERPRISE_TC_PASSWORD` | 24 sampai 32 |

  Login akun pertama (staff `Client Starter`) di hook `before` spec ini. Akun default suite adalah Total Control Client A (Budi Santoso, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.GS_TC_PASSWORD`); hook `after` spec ini mengembalikan sesi ke akun default suite. Halaman awal: Global Settings.
- Environment variable: `GS_STARTER_TC_PASSWORD`, `GS_GROWTH_TC_PASSWORD`, `GS_PROFESSIONAL_TC_PASSWORD`, `GS_ENTERPRISE_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama variabel baru mengikuti pola `<APP>_<ROLE>_PASSWORD` dan belum terdaftar di `spectra.config.ts` dan `.env.example`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun aktor tiap spec, termasuk keempat akun staff di atas; spec ini tidak mengatur flag sendiri.
- State tenant: plan tiap entitas (Starter, Growth, Professional, Enterprise) sudah berlaku di environment automation dan disediakan tim FE; spec ini tidak mengubah plan. Record General Settings tiap entitas berada pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), disediakan tim FE.
- Kemampuan teknis: klien HTTP dengan sesi API akun tiap entitas (kredensial variabel di atas) untuk PUT `/v2/enterprise-management/general-settings` dengan payload baseline `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30`, memulihkan baseline tiap entitas sesudah Save (langkah 7, 15, 23, 32); hook `after` memulihkan ulang walau spec gagal di tengah.
- Data Uji: Session Idle Timeout `1 hour`. Tidak ada Data Dinamis yang dibuat; Save menghasilkan baris Changelog di tiap entitas yang tidak dihapus (audit trail permanen).
- Spec mengubah record empat entitas lain sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`).
- TC-GS-GSET-123: login sebagai Total Control staff tiap entitas dan berada di Global Settings.

## Test Steps

### Plan Starter

1. Buka Global Settings > General Settings lewat menu pada sidebar
2. Verifikasi kelima field tersedia: Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout
3. Verifikasi tidak ada upsell atau limit berbeda
4. Pilih Session Idle Timeout `1 hour`
5. Klik `[Save]`
6. Verifikasi toast sukses: `Success, general settings has been saved.`
7. Pulihkan record `Client Starter` ke baseline lewat PUT API (lihat Prerequisites)

### Plan Growth

8. Ganti akun: Logout, lalu login sebagai Total Control staff `Client Growth` (`Spectra.env.GS_GROWTH_TC_PASSWORD`)
9. Buka Global Settings > General Settings lewat menu pada sidebar
10. Verifikasi kelima field tersedia: Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout
11. Verifikasi tidak ada upsell atau limit berbeda
12. Pilih Session Idle Timeout `1 hour`
13. Klik `[Save]`
14. Verifikasi toast sukses: `Success, general settings has been saved.`
15. Pulihkan record `Client Growth` ke baseline lewat PUT API (lihat Prerequisites)

### Plan Professional

16. Ganti akun: Logout, lalu login sebagai Total Control staff `Client Professional` (`Spectra.env.GS_PROFESSIONAL_TC_PASSWORD`)
17. Buka Global Settings > General Settings lewat menu pada sidebar
18. Verifikasi kelima field tersedia: Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout
19. Verifikasi tidak ada upsell atau limit berbeda
20. Pilih Session Idle Timeout `1 hour`
21. Klik `[Save]`
22. Verifikasi toast sukses: `Success, general settings has been saved.`
23. Pulihkan record `Client Professional` ke baseline lewat PUT API (lihat Prerequisites)

### Plan Enterprise

24. Ganti akun: Logout, lalu login sebagai Total Control staff `Client Enterprise` (`Spectra.env.GS_ENTERPRISE_TC_PASSWORD`)
25. Buka Global Settings > General Settings lewat menu pada sidebar
26. Verifikasi kelima field tersedia: Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout
27. Verifikasi tidak ada upsell atau limit berbeda
28. Pilih Session Idle Timeout `1 hour`
29. Klik `[Save]`
30. Verifikasi toast sukses: `Success, general settings has been saved.`
31. Verifikasi kesimpulan: tidak ada upsell atau limit berbeda pada keempat plan (hasil langkah 3, 11, 19, dan 27)
32. Pulihkan record `Client Enterprise` ke baseline lewat PUT API (lihat Prerequisites)

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Kelas state tenant (prinsip 13h): perbandingan plan tier tanpa gating; keempat entitas berbagi langkah identik (buka, verifikasi lima field, ubah Session Idle Timeout, Save), hanya akun login yang berbeda.
- Pemetaan Expected TC-GS-GSET-123: a ke langkah 2 dan 6; b ke 10 dan 14; c ke 18 dan 22; d ke 26 dan 30. Klausa "tidak ada upsell atau limit berbeda pada keempat plan" pada Expected d diasersi per plan di langkah 3, 11, 19, dan 27, lalu disimpulkan atas keempat sesi di langkah 31.
- Dua akun atau lebih dalam satu spec sah (konvensi bagian 3, pemisah "beda akun"): ada Step ganti akun eksplisit (langkah 8, 16, 24) dan tiap blok tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung: langkah 7, 15, 23, dan 32 (memulihkan baseline tiap entitas lewat API).
- Temuan untuk QA:
  - TC-GS-GSET-123: email akun staff `Client Starter`, `Client Growth`, `Client Professional`, dan `Client Enterprise` tidak ada di Tabel Data Uji Pre-setup (hanya entitas No 20 sampai 23); akun dan keadaan plan disediakan tim FE.
  - TC-GS-GSET-123: TC tidak mencantumkan precondition record General Settings tersimpan; spec mengasumsikan baseline Pre-setup No 10 untuk tiap entitas.
  - TC-GS-GSET-123: Expected d "tidak ada upsell atau limit berbeda pada keempat plan" tidak menyebut elemen UI yang diamati; spec mengasersinya sebagai `Verifikasi` di tiap blok plan (langkah 3, 11, 19, dan 27) dan menyimpulkannya di langkah 31.
