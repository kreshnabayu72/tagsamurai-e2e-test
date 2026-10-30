---
id: TC-GS-DIV-E2E-051-resilience-export-gagal-download-tabel-dan-changelog
title: "Resilience Export: Kegagalan Download Tabel Division dan Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-186
  - TC-GS-DIV-223
coverage:
  web: automated
---

# Resilience Export: Kegagalan Download Tabel Division dan Changelog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness fault injection, prinsip 13b konvensi).
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Asersi spec ini tidak bergantung pada kumpulan nama atau jumlah baris, sehingga Population D-02 tidak di-seed.
- Data Dinamis milik spec: Division `Resilience Export {runId}-051` (Code auto-generate, tidak diasersi) dibuat lewat kemampuan seeding Division lewat API di hook `before` oleh akun Total Control (Sari D) agar Riwayat Changelog Division terisi (precondition TC-GS-DIV-223). Hook `after` menghapus Division tersebut lewat API tanpa berasumsi seeding berhasil penuh. Entri Changelog tidak dihapus (immutable).
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit:
  - Respons export tabel Division (`Download CSV`): endpoint `POST /v2/iam/divisions/export` (LLD `low-level-design.md`, `openapi.yaml`); jawab 500 tanpa meneruskan request ke server (TC-GS-DIV-186).
  - Respons export Changelog Division (`Download CSV`): jawab 500 tanpa meneruskan request ke server (TC-GS-DIV-223); endpoint export Changelog tidak ada di LLD maupun `openapi.yaml`, sehingga ditentukan tim FE.
- Kemampuan teknis: mengamati bahwa tidak ada berkas terunduh (event download browser).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): semua intercept dilepas; Division seeding dihapus; Modal Changelog ditutup. Spec tidak mengubah data Division selain seeding itu.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-DIV-186: Download gagal menampilkan toast error

1. Pasang intercept pada respons export tabel Division: jawab 500
2. Klik icon Download
3. Klik `Download CSV`
4. Verifikasi toast error `Error, failed to download Division.`
5. Verifikasi tidak ada berkas terunduh
6. Lepas intercept respons export tabel Division

### TC-GS-DIV-223: Download Changelog gagal menampilkan toast error

7. Klik icon Changelog di Table Tools
8. Pasang intercept pada respons export Changelog Division: jawab 500
9. Klik icon Download pada Modal Changelog
10. Klik `Download CSV`
11. Verifikasi toast error `Error, failed to download Changelog-Division.`
12. Lepas intercept respons export Changelog Division
13. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE (intercept parsial dan state backend nyata; kelas harness fault injection).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (186, 223) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 dan 12 (melepas intercept segera setelah pemicu), langkah 13 (menutup Modal Changelog).
- Kegagalan export tabel (TC-GS-DIV-186) dan export Changelog (TC-GS-DIV-223) sama-sama kegagalan respons HTTP yang dapat dipicu lewat intercept.
- Pembagian TC lintas spec: isi berkas Download tabel (TC-GS-DIV-180 sampai 185, 187) ada di spec 050; isi berkas Download Changelog (TC-GS-DIV-221, 222) ada di spec 063.
- Temuan untuk QA:
  - TC-GS-DIV-186 Expected b ("Tidak ada file terunduh") diasersi lewat event download browser; TC-GS-DIV-223 tidak memuat Expected tentang berkas, sehingga tidak ada asersi serupa di blok TC-GS-DIV-223.
  - TC-GS-DIV-186 dan 223: TC tidak menyebut endpoint export yang di-intercept maupun cara memaksa respons 500; endpoint export tabel diambil dari LLD, endpoint export Changelog tidak ada di LLD dan ditulis sebagai kebutuhan untuk tim FE (tidak mengarang endpoint).
  - TC-GS-DIV-223: Precondition riwayat Changelog dengan Modified By Sari D, Rina M, Agus W, Dewi L tidak diperlukan oleh asersinya; spec hanya memerlukan riwayat tidak kosong lewat satu Division seeding oleh Sari D, dengan asumsi seeding lewat API menghasilkan entri Create di Changelog (tidak dinyatakan TC dan PRD).
