---
id: TC-GS-USER-E2E-095-list-kolom-name-dan-access-tampilan
title: 'Tampilan kolom Name dan Access di User List dan User Detail'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-177
  - TC-GS-USER-466
  - TC-GS-USER-460
coverage:
  web: automated
---

# Tampilan kolom Name dan Access di User List dan User Detail

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data mock: user "Muhammad Alexander Christian Prawiranegara" (nama lebih dari 30 karakter), dan user dengan Access ke Global Settings dan Admin Console yang di-assign dalam urutan Global Settings dulu

## Test Steps

1. Amati kolom Name pada baris "Muhammad Alexander Christian Prawiranegara"
2. Verifikasi avatar dan nama lengkap tampil utuh (wrap alami) tanpa dipotong dengan `..`
3. Hover atau fokus dengan keyboard pada nama
4. Verifikasi tooltip menampilkan nama lengkap
5. Amati kolom Access pada user yang di-assign Global Settings lebih dulu
6. Verifikasi badge tampil alfabetis "Admin Console" lalu "Global Settings" terlepas dari urutan assignment
7. Urutkan kolom lain (mis. klik header Name) dan verifikasi urutan badge dalam satu sel tidak berubah
8. Verifikasi chip Access memakai badge severity Dark (bukan Secondary) di kolom List
9. Buka User Detail user yang sama dan verifikasi chip Access memakai severity Dark yang sama

## Notes

- Sumber `user.md` bagian 4.2a dan 4.4, serta `prd-conventions.md` bagian 9.13 dan 9.14 (kolom entitas utama tidak dipotong, hanya badge kontekstual yang dipotong).
