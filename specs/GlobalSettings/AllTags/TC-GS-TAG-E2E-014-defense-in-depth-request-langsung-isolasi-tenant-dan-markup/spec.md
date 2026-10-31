---
id: TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup
title: "Defense-in-Depth: Request Langsung Tanpa Capability/Read Only/Read, Isolasi Tenant, Kolisi Tanpa Kebocoran, dan Markup sebagai Teks"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-34
  - TC-GS-TAG-323
  - TC-GS-TAG-324
  - TC-GS-TAG-325
  - TC-GS-TAG-326
  - TC-GS-TAG-374
  - TC-GS-TAG-375
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Tanpa Capability/Read Only/Read, Isolasi Tenant, Kolisi Tanpa Kebocoran, dan Markup sebagai Teks

## Prerequisites

- Mode: FE+BE.
- Spec kelas a (defense-in-depth). Request langsung ke server dikirim lewat klien HTTP (tanpa melewati browser) dengan sesi API masing-masing role; asersinya hanya respons server (status) dan state data (dibaca lewat kemampuan baca fixture BE yang disediakan tim FE/BE). Pengalihan halaman, toast, dan tampilan tidak diasersi pada langkah request langsung (8b butir 1). Endpoint dan payload request ditentukan tim FE dari `openapi.yaml` di tahap script; tidak dikarang di spec.
- Login akun aktor UI pertama (Total Control Client B) di hook `before`; ganti akun ke Total Control Client A ditulis sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.

Akun yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Client | Email | Env var password | Sarana |
|---|---|---|---|---|---|
| TC-34 | Manage TAG (Read), Tono Hartono | A | `manageTagRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TAG_READ_PASSWORD` | sesi API |
| TC-323 | Read Only, Maya Putri | A | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` | sesi API |
| TC-374 | Manage asset & TAG (Read) FAMS, Bayu Prasetyo | A | `manageAssetTagRead_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_FAMS_ASSETTAG_READ_PASSWORD` | sesi API |
| TC-375 | Tanpa Kapabilitas, Rina Marlina | A | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` | sesi API |
| TC-324 | Total Control, Kartika Sari | B | `totalControl_automated_qaTeam2@qwertysystem.net` | `Spectra.env.GS_CLIENTB_TC_PASSWORD` | UI dan sesi API |
| TC-325, TC-326 | Total Control, Sari Dewi | A | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` | UI |

- `GS_TAG_READ_PASSWORD` dan `GS_FAMS_ASSETTAG_READ_PASSWORD` belum terdaftar di `.env.example` dan `spectra.config.ts` (dicatat di `suite.md` bagian Kredensial).
- Data Pre-setup (hanya dibaca kecuali yang tertulis): Seed Registri A (DD-01 `E2801160600002054D8A0001`, DD-02 `E2801160600002054D8A0002` Available sebagai target request ditolak); stok resmi Client A DD-S1 (GPS `356938035643001`); IMEI `356938035643201` (DD-N4) In Use di Client B dengan Device Name `Rahasia-B` (TC-325); IMEI `356938035643101` (DD-N1) tidak ada di stok dan tidak In Use di client mana pun sehingga langsung Activated; tidak ada baris Waiting for Approval sehingga dialog informasi "Your activation is pending review." (D-08) tidak muncul (TC-326); opsi mandiri Client A aktif; katalog Client A memuat Device Name `Queclink GV300`. Data di-seed ulang idempotent oleh hook `before`; tag yang diaktivasi TC-325 dan TC-326 dikembalikan ke kondisi awal oleh reset seed pada hook `after` (Q-4; mekanisme disediakan tim FE/BE).
- Baseline log (S-12): jumlah entri Event Log (kedua tab) dan Activity Log Client A dibaca lewat kemampuan baca disediakan tim FE/BE, dicatat sebelum request pertama tiap blok TC-34, TC-323, dan TC-374 (langkah 1, 7, 18).
- Kemampuan teknis: klien HTTP dan sesi API per role (di atas); deteksi dialog JavaScript (`alert`) pada halaman untuk TC-326; kontrol penutup dialog informasi "Your activation is pending review." (TC-325); Template Self-Purchased tidak mensyaratkan pembaca berkas.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach` untuk akun hook; setelah ganti akun, halaman dibuka lewat langkah.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` disetel true untuk akun UI oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: overlay Select TAG Type, Template Self-Purchased, input entri manual GPS, tabel staging, dan popup TAG Log belum punya ID/aria-label di sumber; diselesaikan tim FE di tahap script.
- State global: tidak ada yang diubah selain data registri (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-34: Manage TAG (Read) mengeksekusi aksi tulis lewat endpoint langsung ditolak server

1. Catat baseline jumlah entri Event Log dan Activity Log Client A
2. Kirim permintaan Delete DD-02 langsung ke server memakai sesi Manage TAG (Read), tanpa lewat UI
3. Verifikasi permintaan ditolak 403 Forbidden
4. Verifikasi tag DD-02 tetap ada di registri (state data)
5. Verifikasi jumlah entri Event Log tetap sama dengan baseline
6. Verifikasi jumlah entri Activity Log tetap sama dengan baseline

### TC-GS-TAG-323: Aksi tulis langsung dari role Read Only: Activate, Audit, Delete ditolak server tanpa efek

7. Catat baseline jumlah entri Event Log dan Activity Log Client A
8. Kirim permintaan Activate IMEI `356938035643001` langsung ke server memakai sesi Read Only
9. Verifikasi permintaan Activate ditolak 403
10. Kirim permintaan Submit Audit RFID langsung ke server memakai sesi Read Only (payload disediakan tim FE)
11. Verifikasi permintaan Submit Audit ditolak 403
12. Kirim permintaan Delete DD-02 langsung ke server memakai sesi Read Only
13. Verifikasi permintaan Delete ditolak 403
14. Verifikasi tidak ada tag baru `356938035643001` (state data)
15. Verifikasi status tag DD-02 tidak berubah
16. Verifikasi jumlah entri Event Log tetap sama dengan baseline
17. Verifikasi jumlah entri Activity Log tetap sama dengan baseline

### TC-GS-TAG-374: Role FAMS Manage asset & TAG: pengecualian hanya Popup TAG Log, registri dan aksi tulis tetap ditolak server

18. Catat baseline jumlah entri Event Log dan Activity Log Client A
19. Kirim permintaan baca daftar registri tag langsung ke server memakai sesi Manage asset & TAG (Read) FAMS
20. Verifikasi permintaan baca registri ditolak 403 Forbidden
21. Kirim permintaan Delete DD-02 langsung ke server memakai sesi yang sama
22. Verifikasi permintaan Delete ditolak 403 Forbidden
23. Verifikasi tag DD-02 tetap ada di registri (state data)
24. Kirim permintaan baca TAG Log DD-01 langsung ke server memakai sesi yang sama
25. Verifikasi permintaan baca TAG Log DD-01 berhasil
26. Verifikasi respons mengembalikan entri riwayat DD-01
27. Verifikasi jumlah entri Event Log tetap sama dengan baseline
28. Verifikasi jumlah entri Activity Log tetap sama dengan baseline

### TC-GS-TAG-375: Role tanpa Manage TAG dan tanpa Manage asset & TAG: baca TAG Log langsung ditolak server

29. Kirim permintaan baca TAG Log DD-01 langsung ke server memakai sesi Tanpa Kapabilitas
30. Verifikasi permintaan ditolak 403 Forbidden
31. Verifikasi respons tidak mengembalikan data riwayat DD-01

### TC-GS-TAG-324: Isolasi tenant: client lain tidak dapat melihat atau menghapus tag Client A

32. Ketik Search `E2801160600002054D8A0002` di registri Client B, tekan Enter
33. Verifikasi empty state `No results found`
34. Kirim permintaan Delete untuk tag DD-02 langsung dari sesi Client B
35. Verifikasi permintaan Delete ditolak server (status penolakan; kode persis tidak ditetapkan TC)
36. Kirim permintaan baca TAG Log DD-02 langsung dari sesi Client B
37. Verifikasi respons tidak mengembalikan data DD-02
38. Verifikasi tag DD-02 tetap ada di registri Client A (state data)

### TC-GS-TAG-325: Kolisi tidak membocorkan data client lain

39. Logout, lalu login sebagai Total Control Client A
40. Buka Global Settings > TAG > Tab All
41. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
42. Isi Template Self-Purchased Device Name `Queclink GV300` dan Brand `Queclink`
43. Ketik `356938035643201` di input entri manual, klik `Add`
44. Klik `Submit`, klik `Submit` pada dialog `Submit Activation`
45. Tutup dialog informasi "Your activation is pending review." (kontrol penutup disediakan tim FE)
46. Tunggu aksi selesai
47. Klik item sidebar `TAG`, klik Tab All
48. Ketik Search `356938035643201`, tekan Enter
49. Verifikasi baris `356938035643201` berstatus Waiting for Approval
50. Verifikasi baris hanya memuat data Template Client A
51. Verifikasi baris tidak memuat teks `Rahasia-B`
52. Buka menu baris `356938035643201`, klik `TAG Log`
53. Verifikasi TAG Log hanya memuat data Template Client A
54. Verifikasi TAG Log tidak memuat teks `Rahasia-B`
55. Verifikasi TAG Log dan baris tidak memuat nama, brand, atau identitas Client B
56. Tutup popup, klik `(←)` pada kotak Search

### TC-GS-TAG-326: Brand dan Device Name berisi markup dirender sebagai teks di registri, staging, dan TAG Log

57. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
58. Isi Template Device Name `Queclink GV300`, Brand `<img src=x onerror=alert(1)>`
59. Ketik `356938035643101` di input entri manual, klik `Add`
60. Verifikasi tabel staging menampilkan Brand sebagai teks literal `<img src=x onerror=alert(1)>`
61. Verifikasi tidak ada dialog `alert` yang muncul
62. Klik `Submit`, klik `Submit` pada dialog `Submit Activation`
63. Tunggu aksi selesai
64. Klik item sidebar `TAG`, klik Tab All
65. Ketik Search `356938035643101`, tekan Enter
66. Verifikasi badge Brand baris `356938035643101` menampilkan teks literal
67. Arahkan kursor ke badge Brand baris `356938035643101`
68. Verifikasi tooltip menampilkan `<img src=x onerror=alert(1)>` sebagai teks literal
69. Verifikasi tidak ada dialog `alert` yang muncul di registri
70. Buka menu baris `356938035643101`, klik `TAG Log`
71. Verifikasi TAG Log menampilkan nilai sebagai teks literal
72. Verifikasi tidak ada dialog `alert` yang muncul di TAG Log
73. Tutup popup, klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Sections 2 dan 8). Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: urutan sumber TC-34, TC-323, TC-324, TC-325, TC-326, TC-374, TC-375. Spec memakai TC-34, TC-323, TC-374, TC-375, TC-324, TC-325, TC-326 agar seluruh blok request langsung (sesi API, tanpa UI) berurutan, TC-324 (UI Client B) memakai akun hook, dan aksi yang membuat data (TC-325, TC-326, ganti akun ke Client A) ada di akhir.
- Keputusan D-2 (plan): TC-34, 316c (spec 010), 323, 324 (sebagian), 325, 374, 375 tetap di E2E sebagai defense-in-depth; asersi request langsung hanya status respons dan state data.
- Asersi absence log (TC-34, 323, 374) memakai baseline jumlah entri (D-1, S-12) dengan anchor positif respons 403 (langkah 3, 9/11/13, 20/22) sebelum asersi jumlah. Tidak ada spec absence terpisah. P-1 (S-05): klausa absence log dan asersi jumlah entri tetap TC-34, TC-323, dan TC-374 berada di spec asal; baseline dicatat sebelum request pertama tiap blok (langkah 1, 7, 18).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 7, 18 (baseline), 39 sampai 41 (ganti akun dan membuka halaman; ganti akun eksplisit, S-07), langkah 45 (menutup dialog informasi D-08 sebelum navigasi), langkah 46 dan 63 (Tunggu aksi selesai), langkah 47 dan 64 (kembali ke List: halaman Activate tetap terbuka sesudah commit, sehingga Search registri didahului sidebar `TAG` dan Tab All), langkah 56 dan 73 (menutup popup dan mengosongkan Search), langkah 67 (hover badge Brand untuk mengamati tooltip). Langkah 49 (`Verifikasi` baris berstatus Waiting for Approval) berasal dari langkah 6 TC-325 ("hingga baris berstatus Waiting for Approval") dan sekaligus anchor positif bahwa baris tampil sebelum asersi absence langkah 51; langkah 54 dan 55 menjalankan klausa "tidak ada nama, brand, atau identitas Client B" pada TAG Log dan baris. Langkah 33 (`No results found`) adalah anchor positif absence hasil Search.
- Alasan spec melewati sekitar 35 langkah (73): semua blok kelas a (defense-in-depth) dengan tujuh TC sumber; tiap blok berdiri sendiri (akun, sesi, dan data berbeda) dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah request dan `Verifikasi` status dipecah per request dan per klausa (S-01). Blok TC-325 dan TC-326 memakai UI (kelas a, Tipe Security) sehingga tetap di spec ini.
- Spec memuat blok bukan pembuat data (TC-34, TC-323, TC-374, TC-375, TC-324: request langsung dan pembacaan) dan blok pembuat data (TC-325 dan TC-326: Activate GPS Self-Purchased) tanpa dipecah: semuanya satu kelas (a, defense-in-depth) pada permukaan registri dan Activate Client A; blok pembuat data ada di akhir sehingga kegagalan keras di dalamnya tidak menutupi hasil blok request langsung, dan pembersihan data dilakukan reset seed pada hook `after`.
- Temuan untuk QA:
  - TC-34 butir c, TC-323, dan TC-374 butir c: "tidak ada entri Event Log maupun Activity Log baru" dipetakan sebagai baseline jumlah entri (Event Log dan Activity Log Client A); cara membaca jumlah tidak ditetapkan TC (disediakan tim FE/BE).
  - TC-34 langkah 2 ("Muat ulang halaman registri") adalah observasi UI untuk request langsung; spec tidak mengasersi UI (8b butir 1), melainkan state data. Perilaku FE pada respons 403 tidak diasersi.
  - TC-323 langkah 1 tidak menyebut payload Submit Audit; spec menulis "payload disediakan tim FE".
  - TC-324 Expected b menulis "ditolak server" tanpa kode status dan "tidak mengembalikan data DD-02" tanpa bentuk respons.
  - TC-325 langkah 7 ("Buka baris tersebut dan TAG Log-nya") tidak menyebut cara membuka baris; spec membuka TAG Log lewat menu baris (S-13).
  - TC-326 Brand `<img src=x onerror=alert(1)>` berjumlah 28 karakter sehingga badge registri terpotong sesuai aturan 12+..+12 (TC-8); TC tidak membahas pemotongan. Spec mengasersi hover tooltip sebagai teks literal penuh (langkah 67 dan 68; asersi tambahan di luar Expected TC, dicatat di sini sesuai S-03).
  - TC-326 tidak menyebut cara mendeteksi "tidak ada skrip berjalan"; spec memakai deteksi dialog `alert` (kemampuan teknis).
  - TC-374 langkah 1 menyebut "permintaan baca daftar registri tag" tanpa endpoint; endpoint ditentukan tim FE dari `openapi.yaml`.
  - Post Condition semua TC bernilai `-`.
