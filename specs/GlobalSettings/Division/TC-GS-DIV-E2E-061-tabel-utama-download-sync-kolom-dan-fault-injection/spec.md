---
id: TC-GS-DIV-E2E-061-tabel-utama-download-sync-kolom-dan-fault-injection
title: "Ekspor Berdasarkan Visibilitas Kolom Setup Column dan Ketahanan Terhadap Kegagalan Server 500 Toast Error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-183
  - TC-GS-DIV-184
  - TC-GS-DIV-186
coverage:
  web: automated
---

# Ekspor Berdasarkan Visibilitas Kolom Setup Column dan Ketahanan Terhadap Kegagalan Server 500 Toast Error

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept())
- Kebutuhan mock: intercept endpoint export download untuk simulasi kegagalan server 500
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Download hanya mengekspor kolom yang visible (TC-GS-DIV-183)

1. Hilangkan centang kolom `Code` lewat Overlay Column Visibility
2. Klik Download lalu `Download CSV`
3. Buka file hasil unduhan
4. Verifikasi File hanya memuat kolom `Name` dan `Last Updated`; kolom `Code` tidak ikut
5. Verifikasi Tanpa toast atau peringatan partial export

### Kolom yang di-unhide kembali ikut diekspor (TC-GS-DIV-184)

6. Hilangkan lalu centang kembali kolom `Code`
7. Klik Download lalu `Download CSV`
8. Buka file hasil unduhan
9. Verifikasi File memuat kolom `Name`, `Code`, dan `Last Updated`

### Download gagal menampilkan toast error (TC-GS-DIV-186)

10. Paksa respons Download gagal 5xx
11. Klik Download lalu `Download CSV`
12. Verifikasi Muncul toast error: `Error, failed to download Division.`
13. Verifikasi Tidak ada file terunduh

## Notes

- Memvalidasi bahwa berkas ekspor hanya memuat kolom yang sedang visible (kolom hidden dikeluarkan), kolom yang di-unhide kembali ikut diekspor, dan kegagalan download memunculkan toast T-01: "Error, failed to download Division." (PRD §4.1.1, §6 T-01).
- Sumber pemetaan test case granular: TC-GS-DIV-183, TC-GS-DIV-184, TC-GS-DIV-186.
