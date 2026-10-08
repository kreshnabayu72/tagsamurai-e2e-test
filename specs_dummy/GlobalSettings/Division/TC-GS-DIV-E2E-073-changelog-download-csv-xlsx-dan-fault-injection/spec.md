---
id: TC-GS-DIV-E2E-073-changelog-download-csv-xlsx-dan-fault-injection
title: "Ekspor Riwayat Modal Changelog ke Berkas CSV dan XLSX Berdasarkan Filter Aktif Serta Penanganan Kegagalan Server 500 Toast Error"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-221
  - TC-GS-DIV-222
  - TC-GS-DIV-223
coverage:
  web: automated
---

# Ekspor Riwayat Modal Changelog ke Berkas CSV dan XLSX Berdasarkan Filter Aktif Serta Penanganan Kegagalan Server 500 Toast Error

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi riwayat
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)

## Test Steps

### Download Changelog tanpa Search dan Filter mengekspor seluruh riwayat (TC-GS-DIV-221)

1. Klik icon Changelog di Table Tools
2. Klik Download lalu `Download CSV`
3. Verifikasi File bernama `Changelog-Division.csv` terunduh
4. Verifikasi File memuat seluruh riwayat (bukan hanya halaman yang tampil) dan tidak ada toast sukses

### Download Changelog dengan Filter aktif hanya mengekspor baris yang cocok (TC-GS-DIV-222)

5. Klik icon Changelog di Table Tools
6. Filter Action = `Delete` lalu Apply
7. Klik Download lalu `Download XLSX`
8. Verifikasi File bernama `Changelog-Division.xlsx` terunduh
9. Verifikasi File hanya memuat baris Action `Delete`

### Download Changelog gagal menampilkan toast error (TC-GS-DIV-223)

10. Klik icon Changelog di Table Tools
11. Paksa respons Download gagal 5xx
12. Klik Download lalu `Download CSV`
13. Verifikasi Muncul toast error: `Error, failed to download Changelog-Division.`

## Notes

- Memvalidasi ekspor riwayat mutasi Changelog ke CSV dan XLSX, kepatuhan data terhadap kriteria saringan aktif, dan penanganan toast error saat kegagalan server terjadi (PRD §4.1.2, §5, §6 T-01).
- Sumber pemetaan test case granular: TC-GS-DIV-221, TC-GS-DIV-222, TC-GS-DIV-223.
