---
id: TC-FA-FAAL-E2E-035-search-tab-user-action-reveal-dan-kolom
title: "Search Tab User Action: Reveal Input dan Pencarian Kolom Action, Object, Field, Name, Old Value, New Value, serta Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-118
  - TC-FA-FAAL-119
  - TC-FA-FAAL-120
  - TC-FA-FAAL-121
  - TC-FA-FAAL-122
coverage:
  web: automated
---

# Search Tab User Action: Reveal Input dan Pencarian Kolom Action, Object, Field, Name, Old Value, New Value, serta Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session); langkah 1 membuka Tab User Action. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #12 (Tab User Action UA-01 sampai UA-15, tanggal 18/06/26 Asia/Jakarta), hanya dibaca dan tidak diubah. Baris yang dipakai: UA-01 (Assign, Total Control, Budi Santoso, Admin Alpha), UA-02 (Edit, Groups, `Gedung A > Lantai 3 - Renovasi`, Admin Alpha), UA-03 (Delete, Categories, Electronic Devices, Admin Beta), UA-04 (Report Disposal, Disposal, `Kendaraan Operasional (AST-2024-0088)`, Field Status, Admin Alpha), UA-05 (Report Damaged, Damaged, `Kamera DSLR (AST-2024-0141)`, Field Status, Old Value `Borrowed`, Modified By `Ahmad D`), UA-06 (Finish Audit, Audit, Field Status, New Value `Waiting for Approval`, Admin Beta), UA-07 (Assign, Group Role, Citra Lestari, New Value `Assigned`, Admin Alpha), UA-09 (Auto-Revert, Total Control, Dewi Lestari, Admin Alpha), UA-10 (Activate, User, Field Status, Admin Alpha), UA-11 (Create, Groups, Modified By `System`), UA-12 (Remove, Group Role, Old Value `Assigned`, Admin Alpha), UA-15 (Create, Groups, Admin Alpha). Identitas baris dirujuk lewat `Fixture.activity-log.<kunci>` (fixture `fixtures/activity-log.json` disediakan tim FE; nama kunci ditetapkan tim FE).
- Kata kunci untuk langkah berulang (Data Uji TC-FA-FAAL-119 sampai 122). Kolom "Baris yang tampil" adalah Expected TC; kolom Search diacu pada Data Uji TC:

  TC-FA-FAAL-119, langkah 7 sampai 9:

  | Keyword | Kolom | Baris yang tampil |
  |---|---|---|
  | `report` | Action | UA-04 dan UA-05 |
  | `REPORT` | Action | UA-04 dan UA-05 |
  | `categ` | Object | hanya UA-03 |
  | `status` | Field | UA-04, UA-05, UA-06, dan UA-10 |

  TC-FA-FAAL-120, langkah 10 sampai 12:

  | Keyword | Kolom | Baris yang tampil |
  |---|---|---|
  | `Santoso` | Name | hanya UA-01 |
  | `lantai` | Name (`Gedung A > Lantai 3 - Renovasi`) | hanya UA-02 |
  | `AST-2024-0141` | Name | hanya UA-05 |

  TC-FA-FAAL-121, langkah 13 sampai 15:

  | Keyword | Kolom | Baris yang tampil |
  |---|---|---|
  | `Borrowed` | Old Value | hanya UA-05 |
  | `Waiting` | New Value | hanya UA-06 |
  | `ASSIGNED` | New Value (UA-07) dan Old Value (UA-12) | UA-07 dan UA-12 |

  TC-FA-FAAL-122, langkah 16 sampai 18:

  | Keyword | Kolom | Baris yang tampil |
  |---|---|---|
  | `Dahlan` | Modified By | hanya UA-05, tampil sebagai `Ahmad D` |
  | `system` | Modified By | hanya UA-11, Modified By `System` |
  | `Alpha` | Modified By | UA-01, UA-02, UA-04, UA-07, UA-09, UA-10, UA-12, UA-15 (delapan baris Admin A) |

- Jendela Seed Tab User Action: Filter Date `18/06/26` sampai `18/06/26` (memuat UA-01 sampai UA-15), diterapkan di langkah 2 (precondition TC-FA-FAAL-119, 120, 121, 122) sehingga baris yang diasersi hanya baris seed #12; total entri tidak diasersi.
- State yang diubah spec: Filter Date dan Search Tab User Action; Search dikosongkan oleh langkah akhir tiap iterasi, Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab User Action
2. Klik icon Filter, pilih tanggal mulai `18/06/26` dan tanggal akhir `18/06/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-118: Search Tab User Action, reveal input, autofocus, dan placeholder

3. Klik icon Search
4. Verifikasi input Search terbuka
5. Verifikasi kursor langsung fokus di dalam input Search
6. Verifikasi placeholder `Search action, object, or name...`

### TC-FA-FAAL-119: Search kolom Action, Object, dan Field Tab User Action

Untuk setiap baris tabel Prerequisites TC-FA-FAAL-119 (langkah 7 sampai 9):

7. Ketik Search keyword, tekan Enter
8. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil"
9. Kosongkan isi kotak search, tekan Enter

### TC-FA-FAAL-120: Search kolom Name Tab User Action

Untuk setiap baris tabel Prerequisites TC-FA-FAAL-120 (langkah 10 sampai 12):

10. Ketik Search keyword, tekan Enter
11. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil"
12. Kosongkan isi kotak search, tekan Enter

### TC-FA-FAAL-121: Search kolom Old Value dan New Value Tab User Action

Untuk setiap baris tabel Prerequisites TC-FA-FAAL-121 (langkah 13 sampai 15):

13. Ketik Search keyword, tekan Enter
14. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil"
15. Kosongkan isi kotak search, tekan Enter

### TC-FA-FAAL-122: Search kolom Modified By mencocokkan nama lengkap

Untuk setiap baris tabel Prerequisites TC-FA-FAAL-122 (langkah 16 sampai 18):

16. Ketik Search keyword, tekan Enter
17. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil"
18. Kosongkan isi kotak search, tekan Enter

## Notes

- Alasan di atas 35 langkah dengan ekspansi (18 langkah nominal; langkah 7 sampai 9 diulang 4 kali, 10 sampai 12 diulang 3 kali, 13 sampai 15 diulang 3 kali, 16 sampai 18 diulang 3 kali sehingga 45 langkah): kelima TC satu halaman (Tab User Action), satu dataset #12, dan satu kelas fungsional (Search); tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berulang mengikuti idiom "Untuk setiap baris tabel" (butir 8b.7); parameter tiap iterasi ada di tabel Prerequisites dan `Verifikasi` tetap satu per iterasi.
- Langkah penghubung (S-03): langkah 1 (pindah ke Tab User Action karena layar awal suite adalah Tab Session). Langkah "Klik icon Search" TC-FA-FAAL-119 sampai 122 tidak diulang karena input Search sudah terbuka dari langkah 3 dan tetap terbuka selama kotak dikosongkan lewat langkah 9, 12, 15, dan 18.
- Langkah 2 (S-03): menerapkan Filter Date Jendela Seed Tab User Action sesuai precondition d TC-FA-FAAL-119, 120, 121, dan 122.
- Langkah 8, 11, 14, dan 17 menyebut daftar baris seed pada tabel Prerequisites sebagai pembanding positif asersi "hanya" (butir 8b.2).
- Kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14): `Ahmad D` untuk Ahmad Dahlan dan `Admin A` untuk Admin Alpha.
- Temuan untuk QA:
  - TC-FA-FAAL-119 sampai 122 memberi precondition Filter Date Jendela Seed Tab User Action (18/06/26 sampai 18/06/26) agar hasil Search tidak bergantung pada baris log lain; spec menerapkannya di langkah 2 dan mengikuti TC.
  - TC-FA-FAAL-119 pada Expected a tidak memakai kata "hanya" untuk `report` dan `REPORT` (UA-04 dan UA-05 tampil) sedangkan keyword lain memakai "hanya"; spec menulisnya "tampil" untuk `report` dan `REPORT` sesuai TC.
