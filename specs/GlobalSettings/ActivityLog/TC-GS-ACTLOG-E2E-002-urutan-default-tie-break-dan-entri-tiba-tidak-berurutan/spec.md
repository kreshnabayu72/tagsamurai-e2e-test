---
id: TC-GS-ACTLOG-E2E-002-urutan-default-tie-break-dan-entri-tiba-tidak-berurutan
title: "Urutan Default, Tie-break, dan Entri Tiba Tidak Berurutan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-10
  - TC-GS-ACTLOG-11
  - TC-GS-ACTLOG-214
coverage:
  web: automated
---

# Urutan Default, Tie-break, dan Entri Tiba Tidak Berurutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (seed BE di hook `before`, tidak dapat dihasilkan lewat aksi nyata karena stempel waktu dan urutan kedatangan ditentukan TC):
  - Tab Session, tiga entri berstempel identik `14 Jul 2026, 08:10`: Activity `Login` User `John Doe`; Activity `Login` User `Budi Anwar`; Activity `Change Password` User `Siti Nurbaya`; ditambah entri berstempel `14 Jul 2026, 08:02` dan `14 Jul 2026, 16:52` (satu entri tiap stempel, Activity dan User bebas).
  - Tab User Action, tiga entri berstempel identik `14 Jun 2026, 14:05`: Action `Edit` Field `Email`; Action `Edit` Field `Division`; Action `Create` Field `Name`; ditambah entri berstempel `10 Jun 2026, 16:45` dan `15 Jun 2026, 10:20`.
  - Tab User Action, dua entri dari modul berbeda untuk TC-GS-ACTLOG-214: event pertama terjadi `14 Jun 2026, 10:00` tetapi tiba di server sesudah event kedua yang terjadi `14 Jun 2026, 10:05`.
  - Nama subjek (`John Doe`, `Budi Anwar`, `Siti Nurbaya`) dan stempel seed literal (Population D-04) karena asersi urutan bergantung pada singkatan nama, urutan nama (tie-break User A-Z menurut nama lengkap), dan stempel yang ditulis TC; tidak diberi suffix `{runId}`. Seed idempotent (dilewati bila sudah ada), tidak dihapus, suite serial, dan nama itu bukan target aksi tulis spec lain. Log bersifat append-only (ACTLOG-LOGIC-01).
  - Asersi urutan memakai perbandingan relatif antar baris pertama tiap stempel, sehingga tahan baris duplikat bila seed tetap ditulis ulang pada run berikutnya.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri log Session dan User Action dengan stempel waktu dan urutan kedatangan yang ditentukan di atas, bersifat idempotent, serta pembersihan seed bila tim BE menyediakannya; tidak ada endpoint yang dikarang di spec ini.
- General Settings Date Format, Time Format, dan Time Zone memakai nilai default environment (tidak diubah) sehingga stempel tampil seperti `14 Jul 2026, 08:10`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat `suite.md`). Seed log tidak dapat dihapus lewat UI.

## Test Steps

### TC-GS-ACTLOG-10: Urutan default Tab Session, Date terbaru di atas dengan tie-break Activity lalu User

1. Buka Global Settings > Activity Log > Session tanpa mengubah sort apa pun
2. Buka Filter Panel, isi Date dari `14 Jul 2026` sampai `14 Jul 2026`, klik `[Apply]`
3. Atur jumlah baris per halaman ke 100
4. Verifikasi baris pertama berstempel `14 Jul 2026, 16:52` berada di atas baris pertama berstempel `14 Jul 2026, 08:10`
5. Verifikasi baris berstempel `14 Jul 2026, 08:02` berada di bawah baris terakhir berstempel `14 Jul 2026, 08:10`
6. Verifikasi pada stempel `14 Jul 2026, 08:10` baris pertama `Change Password` / `Siti N` berada di atas baris pertama `Login` / `Budi A`, dan baris pertama `Login` / `Budi A` berada di atas baris pertama `Login` / `John D` (Activity A-Z, lalu User A-Z menurut nama lengkap)
7. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-ACTLOG-11: Urutan default Tab User Action, Date terbaru di atas dengan tie-break Action lalu Field

8. Klik tab "User Action" tanpa mengubah sort apa pun
9. Buka Filter Panel, isi Date dari `10 Jun 2026` sampai `15 Jun 2026`, klik `[Apply]`
10. Atur jumlah baris per halaman ke 100
11. Verifikasi baris pertama berstempel `15 Jun 2026, 10:20` berada di atas baris pertama berstempel `14 Jun 2026, 14:05`
12. Verifikasi baris berstempel `10 Jun 2026, 16:45` berada di bawah baris terakhir berstempel `14 Jun 2026, 14:05`
13. Verifikasi pada stempel `14 Jun 2026, 14:05` baris pertama `Create` / `Name` berada di atas baris pertama `Edit` / `Division`, dan baris pertama `Edit` / `Division` berada di atas baris pertama `Edit` / `Email` (Action A-Z, lalu Field A-Z)
14. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-GS-ACTLOG-214: Entri yang tiba tidak berurutan tampil terurut menurut Date

15. Buka Filter Panel, isi Date dari `14 Jun 2026` sampai `14 Jun 2026`, klik `[Apply]`
16. Atur jumlah baris per halaman ke 100
17. Verifikasi baris pertama berstempel `14 Jun 2026, 10:05` tampil di atas baris pertama berstempel `14 Jun 2026, 10:00` (urutan berdasarkan Date, bukan urutan kedatangan)
18. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-10, 11, 214). Tidak ada TC hanya-BE. Kolom Automation TC-214 bernilai `Manual Only`; kebutuhan teknisnya (seed kedatangan tak berurutan) ada di Prerequisites.
- Seluruh TC satu topik (urutan default) atas seed yang sama; bukan kelas e (tidak ada volume ≥ 100 baris).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 2, 9, dan 15 memfilter rentang Date supaya baris seed (bertanggal 2026) terlihat tanpa mengubah sort; langkah 3, 10, dan 16 mengatur 100 baris per halaman supaya baris pertama dan baris terakhir tiap stempel ada di halaman yang sama (asersi posisi memuat langkah menuju keadaannya); langkah 7, 14, dan 18 membersihkan filter sebelum TC berikutnya (S-09). Filter Date tidak mengubah urutan sort default; asersi urutan hanya membandingkan baris seed.
- Nilai kolom User pada langkah 6 ditulis dalam bentuk tampil (`Siti N`, `Budi A`, `John D`) karena kolom User menampilkan nama singkat dengan tooltip nama lengkap (TC-GS-ACTLOG-13); Expected TC menulis nama lengkap.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah `[Apply]`; langkah "Buka Filter Panel" pada langkah 7, 9, 14, 15, dan 18 mengikuti TC-GS-ACTLOG-10, 11, dan 214 serta mengandaikan panel tertutup sesudah `[Apply]`.
  - Expected TC-10 dan TC-11 menulis nama lengkap di kolom User, sedangkan kolom User menampilkan nama singkat (TC-GS-ACTLOG-13); spec mengasersi bentuk tampil.
  - TC-10, TC-11, dan TC-214 menetapkan stempel seed literal pada log append-only tanpa cara pembersihan atau stempel unik per run; spec memakai seed idempotent dan asersi urutan relatif. TC-214 bertanda `Manual Only` padahal Expected terukur.
  - TC-11 dan TC-214 tidak menyebut Object, Name, dan Modified By baris seed; seed bebas pada kolom itu.
  - TC-10 dan TC-11 tidak menyebut cara menemukan baris seed di antara baris lain yang lebih baru; spec memakai Filter Date (langkah penghubung).
