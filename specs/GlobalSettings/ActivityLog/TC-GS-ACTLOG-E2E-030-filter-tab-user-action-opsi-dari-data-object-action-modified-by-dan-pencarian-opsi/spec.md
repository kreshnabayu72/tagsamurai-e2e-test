---
id: TC-GS-ACTLOG-E2E-030-filter-tab-user-action-opsi-dari-data-object-action-modified-by-dan-pencarian-opsi
title: "Filter Tab User Action: Opsi dari Data (Object, Action, Modified By) dan Pencarian Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-165
  - TC-GS-ACTLOG-166
  - TC-GS-ACTLOG-167
  - TC-GS-ACTLOG-170
coverage:
  web: automated
---

# Filter Tab User Action: Opsi dari Data (Object, Action, Modified By) dan Pencarian Opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada empat entitas log-terbatas segar milik spec ini, satu entitas per keadaan log (tabel "Entitas log-terbatas per keadaan"; disediakan tim FE/BE, email ditetapkan tim FE; Tabel Data Uji Pre-setup baris 13), kredensial `Spectra.env.GS_LIMITLOG_TC_PASSWORD` (semua akun Total Control entitas log-terbatas berbagi password ini). Login `Fixture.activityLog.entitasLog030a` di hook `before`; keadaan lain dicapai dengan langkah ganti akun di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Activity Log > tab User Action.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md). Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun `Fixture.activityLog.entitasLog030a` sampai `entitasLog030d` dan halaman Global Settings > Activity Log (kemampuan disediakan tim FE/BE).
- Environment variable: `GS_LIMITLOG_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Alasan entitas log-terbatas: asersi "opsi tepat sama dengan nilai yang ada di data tabel" dan "nilai yang tidak ada di data tidak tampil" (TC-GS-ACTLOG-165, 166, 167) hanya dapat diverifikasi bila himpunan nilai log entitas diketahui dan tertutup; pada Client A yang dipakai bersama seluruh suite, himpunan itu terus bertambah. Log tidak dapat diubah atau dihapus (ACTLOG-LOGIC-01) dan keadaan TC-GS-ACTLOG-165 (Action hanya `Create`, `Edit`, `Delete`) tidak bisa bertahan bersama keadaan TC-GS-ACTLOG-167 (Action `Pair TAG`, `Resend Activation Email`, `Permanently Delete`), sehingga tiap keadaan memakai entitas sendiri yang tidak dipakai spec lain.
- Kemampuan teknis (disediakan tim FE/BE, tanpa mengarang endpoint): seed BE keadaan log keempat entitas di hook `before`, sebelum langkah pertama. Daftar admin Modified By entitas `entitasLog030a` adalah snapshot admin entitas (`Hendra Pratama`, `Wulan`, dan satu admin entitas lain yang belum pernah beraksi, nama ditetapkan tim FE); master User entitas memuat admin lain itu. Kemampuan lain: login ulang (ganti akun) antar entitas.
- Tabel "Entitas log-terbatas per keadaan" (himpunan nilai log tertutup untuk entitas a sampai c; entri lain tidak ada; entitas d memuat nilai berikut dan TC tidak menyatakan himpunan tertutup):

| Entitas | TC | Action | Object | Field | Modified By |
|---|---|---|---|---|---|
| `Fixture.activityLog.entitasLog030a` | TC-GS-ACTLOG-165 | `Create`, `Edit`, `Delete` | `User`, `Brand` | `Name`, `Division`, `Brand Name` | `Hendra Pratama`, `Wulan` |
| `Fixture.activityLog.entitasLog030b` | TC-GS-ACTLOG-166 | tidak dibatasi | `User`, `General Settings`, `Brand`, `Measurement`, `Position`, `Division` | tidak dibatasi | tidak dibatasi |
| `Fixture.activityLog.entitasLog030c` | TC-GS-ACTLOG-167 | `Create`, `Edit`, `Delete`, `Pair TAG`, `Resend Activation Email`, `Permanently Delete` | tidak dibatasi | tidak dibatasi | tidak dibatasi |
| `Fixture.activityLog.entitasLog030d` | TC-GS-ACTLOG-170 | `Create`, `Edit`, `Delete` | `User`, `Brand`, `Role & Permission` | `Division`, `Brand Name` | `Hendra Pratama`, `Wulan` |

- Tabel "Opsi TC-GS-ACTLOG-165" (field yang dibuka, opsi yang harus tampil, contoh opsi yang tidak boleh tampil; parameter pengulangan langkah 2 sampai 6):

| Field | Opsi yang tampil | Opsi yang tidak tampil |
|---|---|---|
| Action | `Create`, `Edit`, `Delete` | `Pair TAG` |
| Object | `User`, `Brand` | Object lain (mis. `Position`) |
| Field | `Name`, `Division`, `Brand Name` | Field lain (mis. `Position Name`) |
| Modified By | `Hendra Pratama`, `Wulan` | admin entitas lain yang belum pernah beraksi |

- Tabel "Pencarian opsi TC-GS-ACTLOG-170" (kata kunci di dalam field; parameter pengulangan langkah 22 sampai 28):

| Field | Kata kunci | Opsi yang tampil | Opsi yang tidak tampil |
|---|---|---|---|
| Action | `cr` | `Create` | `Edit` |
| Object | `role` | `Role & Permission` | `User` |
| Field | `brand` | `Brand Name` | `Division` |
| Modified By | `hen` | `Hendra Pratama` | `Wulan` |

- Nilai yang tidak boleh tampil, dipilih spec karena TC tidak menyebut nilai konkret: Object `Role & Permission` pada entitas `entitasLog030b` (TC-GS-ACTLOG-166) dan Action `Deactivate` pada entitas `entitasLog030c` (TC-GS-ACTLOG-167); keduanya tidak ada di himpunan entitas masing-masing.
- Nilai Pre-setup dipakai literal (bukan bersuffix) karena asersi mengenai himpunan nilai tertutup pada entitas segar; entri Activity Log tidak dibuat oleh spec ini.
- State global: tidak ada yang diubah selain sesi login (ganti akun antar entitas); Filter Panel ditutup di akhir tiap bagian.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-165: Isi opsi filter bersumber dari data tabel

1. Klik icon Filter pada toolbar tab User Action
2. Untuk setiap baris tabel "Opsi TC-GS-ACTLOG-165" (langkah 2 sampai 6): buka daftar opsi field pada kolom "Field"
3. Verifikasi daftar opsi memuat persis opsi pada kolom "Opsi yang tampil" tabel itu
4. Verifikasi opsi pada kolom "Opsi yang tidak tampil" tabel itu tidak tampil
5. Verifikasi tidak ada opsi `None` pada daftar
6. Tutup daftar opsi

### TC-GS-ACTLOG-166: Opsi Object bersumber dari data dan ditulis konsisten dari modul pengirim

7. Ganti akun: Logout, login sebagai Total Control `Fixture.activityLog.entitasLog030b` (`Spectra.env.GS_LIMITLOG_TC_PASSWORD`), buka Global Settings > Activity Log > tab User Action
8. Klik icon Filter
9. Buka daftar opsi field Object
10. Verifikasi opsi Object tepat sama dengan nilai Object di data tabel: `User`, `General Settings`, `Brand`, `Measurement`, `Position`, `Division`
11. Verifikasi opsi Object `Role & Permission` (tidak ada di data tabel) tidak tampil
12. Verifikasi tidak ada opsi kosong atau `None`
13. Tutup daftar opsi

### TC-GS-ACTLOG-167: Opsi Action bersumber dari data dan ditulis persis dari modul pengirim

14. Ganti akun: Logout, login sebagai Total Control `Fixture.activityLog.entitasLog030c` (`Spectra.env.GS_LIMITLOG_TC_PASSWORD`), buka Global Settings > Activity Log > tab User Action
15. Klik icon Filter
16. Buka daftar opsi field Action
17. Verifikasi opsi Action tepat sama dengan nilai Action di data tabel, penulisan identik dengan modul pengirim: `Create`, `Edit`, `Delete`, `Pair TAG`, `Resend Activation Email`, `Permanently Delete`
18. Verifikasi opsi Action `Deactivate` (tidak ada di data tabel) tidak tampil
19. Tutup daftar opsi

### TC-GS-ACTLOG-170: Pencarian di dalam field multi-select

20. Ganti akun: Logout, login sebagai Total Control `Fixture.activityLog.entitasLog030d` (`Spectra.env.GS_LIMITLOG_TC_PASSWORD`), buka Global Settings > Activity Log > tab User Action
21. Klik icon Filter
22. Untuk setiap baris tabel "Pencarian opsi TC-GS-ACTLOG-170" (langkah 22 sampai 28): buka field pada kolom "Field", ketik kata kunci pada kolom "Kata kunci" di kotak pencarian field
23. Verifikasi daftar opsi memuat opsi pada kolom "Opsi yang tampil" tabel itu
24. Verifikasi opsi pada kolom "Opsi yang tidak tampil" tabel itu tidak tampil
25. Ganti kata kunci dengan `zzz`
26. Verifikasi tidak ada opsi yang tampil
27. Verifikasi tidak ada pesan error
28. Tutup daftar opsi

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Alasan spec di atas smell 35 langkah: 28 langkah nominal, sekitar 64 langkah dieksekusi (langkah 2 sampai 6 diulang untuk empat field dan langkah 22 sampai 28 untuk empat field). Semua blok satu topik (opsi dan pencarian opsi Filter Panel Tab User Action), satu kelas harness, dan tiap blok memakai entitas sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pengulangan: langkah 2 sampai 6 diulang untuk empat baris tabel "Opsi TC-GS-ACTLOG-165" dan langkah 22 sampai 28 untuk empat baris tabel "Pencarian opsi TC-GS-ACTLOG-170"; tiap iterasi mengulang `Verifikasi` di dalam blok, sehingga tiap field (empat) punya `Verifikasi` sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 14, 20 (ganti akun ke entitas log-terbatas keadaan TC berikutnya; Filter Panel dan pilihan TC sebelumnya hilang karena login ulang), langkah 6, 13, 19, 28 (menutup daftar opsi).
- Asersi tambahan di luar Expected TC: tidak ada.
- Pembagian TC: TC-GS-ACTLOG-168 ada di spec 051 dan TC-GS-ACTLOG-169 ada di spec 062 (bukan `sourceTc` spec ini). TC-GS-ACTLOG-171 sampai 174 (chip dan overflow) ada di spec 031; TC-GS-ACTLOG-159 sampai 164 ada di spec 029.
- Temuan untuk QA:
  - Precondition TC-GS-ACTLOG-165 (Action hanya `Create`, `Edit`, `Delete`; Modified By hanya dua admin) dan TC-GS-ACTLOG-167 (Action `Pair TAG`, `Resend Activation Email`, `Permanently Delete`) saling bertentangan bila dipasang pada satu entitas yang sama; spec memakai satu entitas segar per keadaan (empat entitas). Baris Pre-setup 13 (satu entitas "subset ...") tidak merinci isi eksak tiap keadaan; TC-GS-ACTLOG-170 hanya menyatakan "Opsi tersedia" tanpa himpunan tertutup.
  - TC-GS-ACTLOG-165 menulis Action `Pair TAG` sebagai contoh opsi yang tidak tampil; Field lain dan Object lain pada spec ini (`Position Name`, `Position`) adalah contoh yang dipilih spec, tidak disebut TC.
  - TC-GS-ACTLOG-166 dan 167 menyatakan "nilai yang tidak ada di data tidak tampil" tanpa nilai konkret; nilai `Role & Permission` dan `Deactivate` dipilih spec.
  - TC-GS-ACTLOG-165 tidak menyebut nama admin entitas lain yang belum pernah beraksi (Expected d: "admin lain tidak tampil"); nama ditetapkan tim FE.
  - TC-GS-ACTLOG-167 dan 166 memakai himpunan nilai yang menuntut aksi nyata modul lain (Pair TAG, Permanently Delete) yang butuh hardware atau File Manager; spec mengandalkan seed BE.
