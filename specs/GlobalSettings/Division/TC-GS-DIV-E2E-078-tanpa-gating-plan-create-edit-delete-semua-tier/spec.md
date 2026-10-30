---
id: TC-GS-DIV-E2E-078-tanpa-gating-plan-create-edit-delete-semua-tier
title: "Tanpa Gating Plan: Create, Edit, dan Delete Identik di Semua Tier"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-280
coverage:
  web: automated
---

# Tanpa Gating Plan: Create, Edit, dan Delete Identik di Semua Tier

## Prerequisites

- Mode: FE+BE. Spec membuat, mengubah, dan menghapus Division, serta mengubah plan Client A (state global).
- Akun: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Plan yang diuji (langkah 1 sampai 18 dilakukan untuk setiap plan pada tabel, berurutan):

  | Urutan | Plan | Expected Result TC-GS-DIV-280 |
  |---|---|---|
  | 1 | Starter | a |
  | 2 | Growth | b |
  | 3 | Professional | c |
  | 4 | Enterprise | d |

- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi): `Plan Check {runId}-078`, dibuat lewat UI, diubah menjadi `Plan Check 2 {runId}-078`, lalu dihapus lewat UI, pada setiap plan. Division ini bebas relasi dan milik spec ini; tidak memakai Division Pre-setup atau Population.
- Kemampuan teknis: mengubah plan Client A lewat API atau alat administrasi (Starter, Growth, Professional, Enterprise) di dalam spec, lalu memuat ulang halaman Division setelah tiap perubahan plan (mekanisme, akun pelaku, dan hak ubah disediakan tim FE; TC, PRD, dan LLD tidak menyebut akun pelakunya).
- Prasyarat environment: Master Data Count Limit Division tidak tercapai pada setiap plan (nilai platform default, tidak diubah spec ini).
- Hook `before` mencatat plan awal Client A. Hook `after` memulihkan plan Client A ke plan awal dan menghapus lewat API `Plan Check {runId}-078` dan `Plan Check 2 {runId}-078` bila ada, tanpa berasumsi langkah spec berhasil penuh.
- Suite berjalan serial (`parallel: false`) karena plan Client A diubah untuk seluruh tenant.
- TC-GS-DIV-280: login sebagai Total Control dan berada di Global Settings > User > Division; entitas uji tersedia pada plan Starter, Growth, Professional, dan Enterprise.

## Test Steps

### TC-GS-DIV-280: Create, Edit, dan Delete identik di semua tier plan tanpa gating

Lakukan langkah 1 sampai 18 untuk setiap plan pada tabel "Plan yang diuji".

1. Ubah plan Client A menjadi plan yang diuji (lewat API atau alat administrasi)
2. Muat ulang halaman Global Settings > User > Division
3. Klik `[+ Division]`
4. Isi Division Name `Plan Check {runId}-078`
5. Klik [Submit]
6. Verifikasi toast sukses: `Success, division has been created.`
7. Verifikasi tidak ada dialog upsell dan tidak ada dialog `Limit Reached`
8. Ketik Search `Plan Check {runId}-078`, tekan Enter pada tabel Division
9. Klik `⋯` pada baris `Plan Check {runId}-078` > Edit
10. Ubah Division Name menjadi `Plan Check 2 {runId}-078`
11. Klik [Save]
12. Verifikasi toast sukses: `Success, division has been updated.`
13. Verifikasi tidak ada dialog upsell dan tidak ada dialog `Limit Reached`
14. Ganti isi kotak search dengan `Plan Check 2 {runId}-078`, tekan Enter pada tabel Division
15. Klik `⋯` pada baris `Plan Check 2 {runId}-078` > Delete
16. Klik [Delete] pada dialog `Delete Division`
17. Verifikasi toast sukses: `Success, division has been deleted.`
18. Verifikasi tidak ada dialog upsell dan tidak ada dialog `Limit Reached`

Sesudah keempat plan selesai:

19. Verifikasi Create, Edit, dan Delete berhasil dengan toast sukses masing-masing pada keempat plan, tanpa gating, upsell, atau dialog `Limit Reached` antar plan
20. Pulihkan plan Client A ke plan awal yang dicatat di hook `before`

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas state tenant (prinsip 13h), jenis plan; hanya satu TC sumber dan tidak ada TC yang terbelah lintas spec.
- Langkah 1 sampai 18 diulang untuk empat plan mengikuti Langkah Uji TC ("Pada tiap plan") dan pola "lakukan untuk setiap baris pada tabel" (analog bagian 3a); langkah verifikasi pada langkah 6, 12, dan 17 menjadi Expected Result a sampai d untuk plan pada baris tabel yang sedang berjalan (Starter, Growth, Professional, Enterprise). Cara skrip menjalankan perulangan diputuskan di tahap script.
- Langkah 19 memuat Expected Result e TC, kesimpulan dari butir a sampai d.
- Langkah penghubung: langkah 1 dan 20 (mengubah dan memulihkan plan Client A; hook `after` menjadi cadangan), langkah 2 (memuat ulang halaman setelah plan berubah), langkah 8 dan 14 (Search nama yang menjadi target baris).
- Langkah 7, 13, dan 18 (tidak ada dialog upsell atau `Limit Reached` pada tiap aksi) adalah asersi tambahan yang memecah Expected Result e per aksi dan per plan; ditulis agar kesimpulan pada langkah 19 punya bukti pada setiap aksi. Klausa "limit berbeda antar plan" pada Expected Result e tidak diasersi karena tidak teramati.
- Spec melewati sekitar 35 langkah bila perulangan dihitung per plan (18 langkah dikali 4 plan, ditambah 2 langkah penutup, setara 74 langkah); satu TC dalam satu kelas harness (state tenant jenis plan). Rantai data: keempat putaran memakai nama Division yang sama, `Plan Check {runId}-078` (Create), `Plan Check 2 {runId}-078` (Edit), lalu Delete pada akhir tiap putaran, sehingga setiap putaran memerlukan Division putaran sebelumnya sudah terhapus.
- Temuan untuk QA:
  - TC-GS-DIV-280: TC tidak menyebut cara mengubah plan Client A; disediakan tim FE sebagai kemampuan teknis tanpa mengarang endpoint.
  - TC-GS-DIV-280: TC tidak menyebut Name Edit selain `Plan Check 2`; spec memakai `Plan Check 2 {runId}-078`, nama yang sama untuk setiap plan karena Division dihapus pada akhir tiap plan.
  - TC-GS-DIV-280: Expected Result e menyebut "limit berbeda antar plan (hanya Master Data Count Limit platform)"; TC tidak menyebut nilai limit pada tiap plan, sehingga spec hanya mengasersi tidak ada dialog `Limit Reached` pada ketiga aksi dan bergantung pada limit tidak tercapai.
