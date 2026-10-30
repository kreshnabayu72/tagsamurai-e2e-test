---
id: TC-GS-ACTLOG-E2E-060-perilaku-identik-di-tiap-tier-plan
title: "Perilaku Identik di Tiap Tier Plan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-224
coverage:
  web: automated
---

# Perilaku Identik di Tiap Tier Plan

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (Total Control tiap Client plan; email akun tidak tertulis di `.env.example` dan ditetapkan tim FE; Client plan dipakai apa adanya tanpa mengubah plan):

| Plan | Akun Total Control | Kredensial |
|---|---|---|
| Starter | Total Control Client plan Starter | `Spectra.env.GS_PLANSTARTER_TC_PASSWORD` |
| Growth | Total Control Client plan Growth | `Spectra.env.GS_PLANGROWTH_TC_PASSWORD` |
| Professional | Total Control Client plan Professional | `Spectra.env.GS_PLANPRO_TC_PASSWORD` |
| Enterprise | Total Control Client plan Enterprise | `Spectra.env.GS_PLANENT_TC_PASSWORD` |

- Login akun plan pertama (Starter) di hook `before`; akun plan berikutnya lewat langkah ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture. Keempat env ini sudah terdaftar di `.env.example` (dipakai Auth > MFA spec 039).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md) untuk akun aktor suite.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control keempat Client plan dan halaman Activity Log (kemampuan disediakan tim FE/BE).
- Pembanding "sama dengan plan Starter" (operasional): (a) tabel menampilkan lebih dari nol baris; (b) jenis baris sama, yaitu Activity `Login` pada Tab Session dan Action `Create` pada Tab User Action; (c) berkas CSV terunduh dan tidak kosong; (d) tidak ada penanda upgrade, pembatasan fitur, atau batas jumlah baris yang tampil pada plan lain tetapi tidak pada Starter.
- Data Pre-setup: keempat Client plan memiliki log yang sama bentuknya (baris Session dan User Action). Data Dinamis: di hook `before`, tiap Client plan di-seed lewat API dengan dua aksi sumber ber-Action berbeda, yaitu Create Brand `Brand Plan {runId}-060` (Action `Create`) lalu Edit Brand yang sama dengan mengganti Brand Name (satu-satunya field Brand) menjadi `Brand Plan {runId}-060 Ubah` (Action `Edit`), sehingga Tab User Action memuat sedikitnya dua nilai Action distinct; baris Session berasal dari login akun plan itu sendiri. Brand dihapus lewat API di hook `after` dengan nama terakhir tanpa berasumsi seeding berhasil penuh; entri log tidak dapat dihapus dan nama bersuffix run mencegah bentrok.
- Kemampuan teknis: mengamati unduhan berkas CSV dan membandingkan hasil antar plan sesuai pembanding di atas; sesi API akun Total Control tiap Client plan (disediakan tim FE/BE) sebagai pelaku seed dan cleanup, tanpa mengarang endpoint.
- Tidak ada plan yang diubah; sesi dikembalikan ke akun default suite di hook `after`. Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-224: Perilaku identik di tiap tier plan

Untuk setiap baris tabel "Role yang diuji" (Starter, Growth, Professional, Enterprise), lakukan langkah 1 sampai 21. Langkah 1 dilewati untuk plan Starter karena sudah login di hook `before`.

1. Ganti akun: login sebagai Total Control Client plan yang sedang diuji
2. Buka Global Settings > Activity Log > Session
3. Verifikasi Tab Session tersedia dengan tabel yang menampilkan baris
4. Ketik Search `Login`, tekan Enter
5. Verifikasi Search Tab Session menampilkan baris dengan Activity `Login`, jenis barisnya sama dengan hasil plan Starter
6. Klik `(←)` pada kotak Search Tab Session
7. Klik icon Filter, pilih Activity `Login`, klik [Apply]
8. Verifikasi Filter Activity Tab Session menampilkan baris dengan Activity `Login`, jenis barisnya sama dengan hasil plan Starter
9. Klik icon Filter, klik [Clear Field] pada field Activity, klik [Apply]
10. Klik icon Download, lalu klik `Download as CSV`
11. Verifikasi Download CSV Tab Session menghasilkan berkas yang tidak kosong, sama perilakunya dengan plan Starter
12. Klik tab "User Action"
13. Verifikasi Tab User Action tersedia dengan tabel yang menampilkan baris
14. Ketik Search `Brand Plan {runId}-060`, tekan Enter
15. Verifikasi Search Tab User Action menampilkan baris yang cocok dengan `Brand Plan {runId}-060`, jenis barisnya sama dengan hasil plan Starter
16. Klik `(←)` pada kotak Search Tab User Action
17. Klik icon Filter, pilih Action `Create`, klik [Apply]
18. Verifikasi Filter Action Tab User Action hanya menampilkan baris dengan Action `Create`, jenis barisnya sama dengan hasil plan Starter
19. Klik icon Download, lalu klik `Download as CSV`
20. Verifikasi Download CSV Tab User Action menghasilkan berkas yang tidak kosong, sama perilakunya dengan plan Starter
21. Verifikasi tidak ada pembatasan, penanda upgrade, atau batas jumlah baris yang berbeda pada kedua tab dibandingkan plan Starter

### Pemulihan state akhir spec

22. Klik icon Filter, klik [Clear Field] pada field Action, klik [Apply]

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Kelas harness h. Spec mengikuti pola Role Matrix: langkah 1 sampai 21 identik untuk setiap plan; hanya akun login yang berbeda. Langkah 21 memperlakukan butir terakhir Expected ("tidak ada pembatasan, penanda upgrade, atau batas jumlah baris yang berbeda") sebagai satu elemen daftar yang disebut utuh. Langkah Filter Action dan Download CSV Tab User Action dipisah menjadi `Verifikasi` tersendiri (langkah 18 dan 20) sesuai pemisahan klausa pada Tab Session (langkah 8 dan 11).
- Spec di atas smell 35 langkah: 22 langkah nominal, 84 langkah dengan ekspansi (langkah 1 sampai 21 dikali empat plan, dikurangi langkah 1 untuk Starter, ditambah langkah 22). Alasan: semua blok satu kelas harness dan identik per plan; hanya akun login yang berbeda dan kegagalan satu plan tidak membuat plan lain kehilangan makna.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (ganti akun eksplisit, S-07); langkah 6, 9, 16, dan 22 (membersihkan Search dan Filter). Pembersihan Filter tiap plan tidak diperlukan sebelum ganti akun karena login baru membuka sesi baru.
- Pembagian TC lintas spec: TC-GS-ACTLOG-222 dan 223 (state tenant) ada di spec 059; TC-GS-ACTLOG-225 (log lama) di spec 061.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 9 dan 22 mengikuti TC-GS-ACTLOG-224.
  - Email keempat akun Total Control Client plan tidak tertulis di `.env.example` maupun tabel Data Uji Pre-setup TC; ditetapkan tim FE.
  - TC-GS-ACTLOG-224 tidak menyebut keyword Search dan nilai Filter; spec memakai `Login` dan Activity `Login` (Tab Session) serta `Brand Plan {runId}-060` dan Action `Create` (Tab User Action).
  - TC-GS-ACTLOG-224 hanya menyebut Download CSV; format lain tidak diuji.
  - Pembanding "perilaku identik" tidak didefinisikan di TC; spec memakai hasil plan Starter sebagai acuan dengan kriteria operasional di Prerequisites.
