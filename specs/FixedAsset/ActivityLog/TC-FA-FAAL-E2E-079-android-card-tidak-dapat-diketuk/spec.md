---
id: TC-FA-FAAL-E2E-079-android-card-tidak-dapat-diketuk
title: "Android: Card Tab Session dan User Action Tidak Dapat Diketuk"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-35
coverage:
  mobile: automated
---

# Android: Card Tab Session dan User Action Tidak Dapat Diketuk

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android Fixed Asset > Reports & Logs > Activity Log.
- Perangkat atau emulator Android dengan aplikasi Fixed Asset TAG Samurai terpasang dan driver perangkat yang mampu mengetuk, menggulir, dan membaca elemen UI; disediakan tim FE. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di aplikasi Android di hook `before` spec ini; spec ini membuka halaman Activity Log sendiri di aplikasi karena hook `beforeEach` suite membuka halaman web. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11, 11 card) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12, 15 card), dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Card yang diasersi: SS-01 (John Doe, Session started, batch kedua) dan UA-01 (card pertama Tab User Action). Spec tidak mengubah data.
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-35: Android: card tidak dapat diketuk

1. Ketuk tab User Action
2. Gulir ke card paling atas
3. Ketuk card UA-01
4. Verifikasi halaman card Tab User Action tetap tampil
5. Verifikasi tidak ada navigasi, drawer, maupun menu yang terbuka
6. Verifikasi card UA-01 hanya informasi
7. Ketuk tab Session
8. Gulir ke bawah hingga card SS-01 tampil
9. Ketuk card SS-01
10. Verifikasi halaman card Tab Session tetap tampil
11. Verifikasi tidak ada navigasi, drawer, maupun menu yang terbuka
12. Verifikasi card SS-01 hanya informasi

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec berjalan di aplikasi Android; `coverage.mobile: automated`. Kemampuan driver Android belum dipastikan tim FE; `coverage` dapat berubah menjadi `unsupported` bila tidak tersedia.
- TC-FA-FAAL-30 sampai 34 ada di spec 008.
- Langkah penghubung (S-03): langkah 1 dan 7 (pindah tab), langkah 2 dan 8 (menggulir ke posisi card yang diasersi).
- Langkah 5 dan 11 (absence navigasi, drawer, menu) berjangkar pada langkah 4 dan 10 (halaman card tetap tampil), diverifikasi sesudah masing-masing ketukan sesuai Expected a dan b TC-FA-FAAL-35.
- Temuan untuk QA:
  - TC-FA-FAAL-35 tidak punya Expected per ketukan dan tidak menyebut kondisi pembanding; spec mengasersi hasil yang sama sesudah tiap ketukan.
