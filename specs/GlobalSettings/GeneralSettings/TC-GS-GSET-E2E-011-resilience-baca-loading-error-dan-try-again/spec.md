---
id: TC-GS-GSET-E2E-011-resilience-baca-loading-error-dan-try-again
title: "Resilience baca halaman"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-03
  - TC-GS-GSET-04
  - TC-GS-GSET-05
coverage:
  web: automated
---

# Resilience baca halaman

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Hook suite (`suite.md`): login akun aktor, flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen, record Client A dipulihkan ke baseline, dan halaman Global Settings > General Settings dibuka di `beforeEach`.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`.
- Data Pre-setup No 10 (record Client A, hanya dibaca): Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit, pada GET `/v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`, operasi `get_general_settings`):
  - Langkah 1 sampai 8 (TC-GS-GSET-03): tahan respons 5 detik lalu jawab normal. Nilai 5 detik adalah data uji, bukan aturan PRD (PRD §7 S-01 hanya menyebut skeleton).
  - Langkah 9 sampai 19 (TC-GS-GSET-04 dan 05): jawab 500 (`{"message": "Internal server error"}`); intercept dilepas di langkah 16 sebelum `[Try Again]`. Tidak dibutuhkan intercept "500 sekali" terpisah.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah. Spec tidak menekan `[Save]` dan tidak mengubah state global.

## Test Steps

### TC-GS-GSET-03: Loading skeleton saat data diambil

1. Pasang intercept pada GET general settings: tahan respons 5 detik lalu jawab normal
2. Buka Global Settings > General Settings (muat ulang halaman, F5)
3. Verifikasi Loading component berupa shimmer skeleton tampil
4. Verifikasi shimmer skeleton mempertahankan proporsi grid form
5. Tunggu respons diterima
6. Verifikasi form terisi nilai tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
7. Verifikasi shimmer skeleton diganti form (skeleton hilang)
8. Lepas intercept pada GET general settings

### TC-GS-GSET-04: Error load saat pembacaan gagal

9. Pasang intercept pada GET general settings: jawab 500
10. Buka Global Settings > General Settings (muat ulang halaman, F5)
11. Verifikasi tampil teks "Unable to load this data."
12. Verifikasi tampil tombol `[Try Again]`
13. Verifikasi tampilan bukan empty state
14. Verifikasi tampilan bukan form kosong

### TC-GS-GSET-05: Try Again memuat ulang data

15. Verifikasi tombol `[Try Again]` masih tampil (state error dari TC-GS-GSET-04)
16. Lepas intercept pada GET general settings agar GET berhasil
17. Klik `[Try Again]`
18. Verifikasi form terisi nilai tersimpan: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`
19. Verifikasi teks "Unable to load this data." hilang

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Kelas harness b (fault injection; `Mode: FE+BE` dengan intercept parsial, bagian 6 konvensi). 19 langkah.
- Dipisah dari spec 020 (resilience Save) dan spec 026 (resilience Changelog) karena gabungan langkahnya melewati batas ukuran jauh (19 + 33 + 20 = 72 langkah, tanpa langkah berulang sehingga ekspansi sama) dan intercept tiap spec berbeda: spec ini mengintercept GET baca halaman, spec 020 mengintercept PUT Save, spec 026 mengintercept request Changelog.
- TC-GS-GSET-05 berdependensi TC-GS-GSET-04; langkah 1 dan 2 TC-GS-GSET-05 (paksa 500, buka halaman) identik dengan langkah 9 dan 10 spec ini, sehingga spec melanjutkan state error dari TC-GS-GSET-04 tanpa membuka ulang halaman, lalu melepas intercept di langkah 16 sebelum `[Try Again]`.
- Langkah penghubung (tanpa `Verifikasi`): langkah 5 (menunggu respons ditahan), 8 (lepas intercept setelah pemicu, S-09), dan 16 (aksi TC-GS-GSET-05 langkah 3). Langkah 15 adalah `Verifikasi` anchor state error sebelum intercept dilepas.
- Absence langkah 7 (skeleton hilang) dan langkah 19 (teks error hilang) didahului `Verifikasi` form terisi (langkah 6 dan 18) pada halaman yang sama.
- Temuan untuk QA:
  - TC-GS-GSET-03 dan TC-GS-GSET-04 tidak menyebut endpoint; spec memakai GET `/v2/enterprise-management/general-settings` dari `openapi.yaml` modul.
  - TC-GS-GSET-04 menyebut "bukan empty state" tanpa menyebut teks empty state halaman form single-record (PRD tidak mendefinisikannya); spec mengasersi tidak ada tampilan empty state.
