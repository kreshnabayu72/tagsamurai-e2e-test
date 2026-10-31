---
id: TC-GS-UOM-E2E-073-tenant-plan-tier-tanpa-gating
title: "Measurement Tidak Digate Plan: Create, Edit, Delete di Starter dan Enterprise serta Upgrade dan Downgrade"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-248
  - TC-GS-UOM-270
coverage:
  web: automated
---

# Measurement Tidak Digate Plan: Create, Edit, Delete di Starter dan Enterprise serta Upgrade dan Downgrade

## Prerequisites

- Mode: FE+BE. Spec membuat dan menghapus unit serta mengubah plan Client A (state global).
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Pengubah plan Client A (hanya lewat API, tanpa login UI) | Total Control (Principal, Hendra Wijaya) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `GS_PRINCIPAL_TC_PASSWORD` |

  Login aktor UI di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Plan yang diuji (parameter langkah berulang pada TC-GS-UOM-248):

  | Urutan | Plan |
  |---|---|
  | 1 | Starter |
  | 2 | Enterprise |

- Kemampuan teknis: mengubah plan Client A (Starter, Enterprise) lewat sesi API aktor (lihat `suite.md`, bagian Hook suite) dengan akun Total Control (Principal) di atas; mekanisme dan endpoint perubahan plan tidak disebut TC dan disediakan tim FE (S-13). Hook `before` mencatat plan awal Client A.
- State global yang dipulihkan (hook `after`, tetap jalan walau spec gagal di tengah): plan Client A dikembalikan ke plan awal yang dicatat hook `before`. Suite berjalan serial (`parallel: false`) dan spec ini tidak berjalan bersama spec Client A lain karena plan diubah untuk seluruh tenant.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi): `Plan Test {runId}-073` / `plt` (dibuat, diedit, dan dihapus spec pada tiap plan) dan `Plan Baru {runId}-073` / `pb` (dibuat spec pada TC-GS-UOM-270). Page size tabel memakai 50 pada TC-GS-UOM-270 agar seluruh baris Client A tampil dalam satu halaman (tabel berisi 20 unit Pre-setup dan Population D-01 ditambah unit milik spec).
- Cleanup (hook `after`): hapus lewat API `Plan Test {runId}-073` dan `Plan Baru {runId}-073` bila ada; pulihkan page size tabel ke 10.
- TC-GS-UOM-248, 270: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-248: Create, Edit, Delete identik di semua tier plan tanpa gating

Untuk setiap plan pada tabel "Plan yang diuji" (Starter, lalu Enterprise) lakukan langkah 1 sampai 11:

1. Ubah plan Client A menjadi plan pada tabel (lewat API dengan akun Total Control Principal)
2. Muat ulang halaman Global Settings > Master Reference > Measurement
3. Klik [+ Unit], isi Unit Name `Plan Test {runId}-073` dan Symbol `plt`, klik [Submit]
4. Verifikasi toast sukses: "Success, unit has been created."
5. Verifikasi tidak ada dialog upgrade dan tidak ada dialog batas kuota
6. Ketik Search `Plan Test {runId}-073`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Symbol menjadi `pt`, klik [Save]
7. Verifikasi toast sukses: "Success, unit has been updated."
8. Verifikasi tidak ada dialog upgrade dan tidak ada dialog batas kuota
9. Klik `⋯` pada baris `Plan Test {runId}-073` > Delete, klik [Delete] pada dialog
10. Verifikasi toast sukses: "Success, unit has been deleted."
11. Verifikasi tidak ada dialog upgrade dan tidak ada dialog batas kuota

### TC-GS-UOM-270: Upgrade dan downgrade plan tidak mengubah data Measurement

12. Ubah plan Client A menjadi Starter (lewat API dengan akun Total Control Principal), muat ulang halaman Measurement, klik `(←)` pada kotak Search, lalu ubah page size tabel menjadi 50
13. Catat jumlah baris Measurement dan Last Updated tiap baris
14. [Principal, sesi API] Upgrade plan Client A ke Enterprise, lalu downgrade ke Starter
15. Muat ulang halaman Measurement, lalu ubah page size tabel menjadi 50
16. Verifikasi jumlah baris Measurement sama dengan langkah 13
17. Verifikasi Last Updated tiap baris sama dengan langkah 13
18. Klik [+ Unit], isi Unit Name `Plan Baru {runId}-073` dan Symbol `pb`, klik [Submit]
19. Verifikasi toast sukses: "Success, unit has been created."
20. Verifikasi tidak ada dialog upgrade dan tidak ada dialog batas kuota

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas state tenant (prinsip 13h): perubahan plan tier dipisah dari verifikasi baca murni.
- Langkah 1 sampai 11 diulang untuk setiap baris tabel "Plan yang diuji" (iterasi dari bagian 8b butir 7); ekspansi: 22 langkah, ditambah 9 langkah TC-GS-UOM-270 menjadi 31 langkah ekspansi. Verifikasi yang diulang tetap satu per klausa.
- Urutan TC: TC-GS-UOM-248 lebih dulu (Starter lalu Enterprise), lalu langkah 12 mengembalikan plan ke Starter sebagai precondition TC-GS-UOM-270 ("Client pada plan Starter"). Seluruh unit yang dibuat dihapus (Plan Test) atau tersisa satu dan dihapus di hook `after` (Plan Baru).
- Langkah penghubung: langkah 1 (mengubah plan sesuai precondition TC "Client pada plan Starter, lalu Enterprise"), langkah 2 dan 15 (muat ulang agar halaman memakai plan terbaru), langkah 6 (Search baris target), langkah 12 (mengatur plan Starter, mengosongkan Search, dan mengatur page size 50), langkah 15 (page size 50 supaya seluruh baris dapat dibandingkan).
- Langkah 5, 8, dan 11 mengasersi "tidak ada dialog upgrade dan tidak ada batas kuota" sebagai satu daftar elemen yang sama-sama tidak ada (S-01), didahului toast sukses sebagai anchor positif; langkah 20 sama.
- Langkah 13 dan 16/17 memakai seluruh baris tabel dalam satu halaman (page size 50); jumlah baris diturunkan dari tabel yang tampil, bukan angka absolut (bagian 8b butir 10).
- Temuan untuk QA:
  - Pelaku dan mekanisme perubahan plan (Starter, Enterprise; upgrade dan downgrade) tidak disebut TC, PRD, atau LLD Measurement (S-13); TC-GS-UOM-270 menyebut "Principal meng-upgrade plan client" tanpa akun dan endpoint. Disediakan tim FE.
  - TC-GS-UOM-248 dan 270 tidak punya Post Condition.
