---
id: TC-GS-TAG-E2E-010-plan-tier-free-downgrade-dan-plan-berbayar
title: "Plan Tier: Free (Activate Hidden, Tag Terkunci), Downgrade ke Free, dan Plan Berbayar Tanpa Pembatasan Antar-Tier"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-315
  - TC-GS-TAG-316
  - TC-GS-TAG-317
  - TC-GS-TAG-318
coverage:
  web: automated
---

# Plan Tier: Free (Activate Hidden, Tag Terkunci), Downgrade ke Free, dan Plan Berbayar Tanpa Pembatasan Antar-Tier

## Prerequisites

- Mode: FE+BE.
- Spec kelas h (state tenant, plan tier). Login akun aktor pertama (Client Free) di hook `before`; ganti akun ditulis sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.

Akun yang diuji (Tabel Data Uji Pre-setup):

| TC | Client / plan | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-315, TC-316 | Client Free (Free) | Joko Widodo | `totalControl_automated_qaFree@qwertysystem.net` | `Spectra.env.GS_TC_FREE_PASSWORD` |
| TC-315 | Client Free, Manage TAG (Update) | akun tidak ada di Pre-setup TC | disediakan tim FE | disediakan tim FE |
| TC-317 | Client Down (downgrade Growth ke Free) | Lukman Hakim | `totalControl_automated_qaDown@qwertysystem.net` | `Spectra.env.GS_TC_DOWN_PASSWORD` |
| TC-318 | Client A (Growth) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-318 | Client Professional | Maria Ulfa | `totalControl_automated_qaProfessional@qwertysystem.net` | `Spectra.env.GS_TC_PROFESSIONAL_PASSWORD` |
| TC-318 | Client Enterprise | Nanda Prakoso | `totalControl_automated_qaEnterprise@qwertysystem.net` | `Spectra.env.GS_TC_ENTERPRISE_PASSWORD` |

- `GS_TC_FREE_PASSWORD`, `GS_TC_DOWN_PASSWORD`, `GS_TC_PROFESSIONAL_PASSWORD`, `GS_TC_ENTERPRISE_PASSWORD` belum terdaftar di `.env.example` dan `spectra.config.ts` (dicatat di `suite.md` bagian Kredensial).
- Data Pre-setup (hanya dibaca kecuali TC-318): Client Free memuat tag QR DD-F1 `TAG-QR-FREE-001` (Paired) dan RFID warisan DD-F2 `E2801160600002054D8A6001` (Available, terkunci). Client Down memuat tag RFID dan tag QR (identifier tidak ditetapkan TC; disediakan tim FE). Client A, Client Professional, dan Client Enterprise masing-masing memuat alokasi GPS dan stok resmi DD-S1 `356938035643001` (GPS Available). Data di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Kemampuan teknis: klien HTTP untuk satu request langsung (Delete DD-F2, TC-316 butir c, dengan sesi Total Control Client Free); pembaca berkas CSV terunduh (untuk Download DD-F2). Tag hasil Activate TC-318 di tiap client dikembalikan ke kondisi awal oleh reset seed pada hook `after`.
- Selektor: ikon gembok, tooltip `Upgrade to unlock`, overlay Select TAG Type, dan input entri manual GPS belum punya ID/aria-label di sumber; diselesaikan tim FE di tahap script.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach` untuk akun hook; setelah ganti akun, halaman dibuka lewat langkah.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` disetel true untuk seluruh akun yang dipakai oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: plan tier tiap client tidak diubah oleh spec (data Pre-setup); jika tim FE menyiapkan plan lewat sesi API, dipulihkan pada hook `after` (daftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-315: Client Free plan: tombol Activate TAG Hidden untuk semua role dan kartu counter tidak tampil

1. Amati toolbar dan area kartu sebagai Total Control Client Free
2. Verifikasi kontrol baca `Search by Scan`, `Search`, `Filter`, `Download` tampil
3. Verifikasi tombol `+ Activate TAG` Hidden
4. Verifikasi tidak ada overlay setelah tombol `+ Activate TAG` dicari
5. Verifikasi tidak ada tooltip pada tombol `+ Activate TAG`
6. Verifikasi kartu License tidak tampil
7. Verifikasi kartu Health tidak tampil
8. Logout, lalu login sebagai Manage TAG (Update) Client Free
9. Buka Global Settings > TAG > Tab All
10. Verifikasi kontrol baca `Search by Scan`, `Search`, `Filter`, `Download` tampil
11. Verifikasi tombol `+ Activate TAG` Hidden
12. Verifikasi tidak ada overlay setelah tombol `+ Activate TAG` dicari
13. Verifikasi tidak ada tooltip pada tombol `+ Activate TAG`
14. Verifikasi kartu License dan Health tidak tampil
15. Logout, lalu login sebagai Total Control Client Free

### TC-GS-TAG-316: Client Free: tag RFID, NFC, BLE, GPS warisan terkunci dan menu baris hanya TAG Log

16. Buka Global Settings > TAG > Tab All
17. Amati sel TAG Type baris DD-F2 `E2801160600002054D8A6001`
18. Verifikasi sel TAG Type baris DD-F2 menampilkan ikon gembok
19. Hover ikon gembok baris DD-F2
20. Verifikasi tooltip `Upgrade to unlock`
21. Buka menu baris DD-F2
22. Verifikasi menu baris hanya berisi `TAG Log`
23. Klik `TAG Log`
24. Verifikasi Popup TAG Log DD-F2 terbuka
25. Tutup popup
26. Ketik Search `E2801160600002054D8A6001`, tekan Enter
27. Verifikasi baris DD-F2 tampil
28. Klik `(←)` pada kotak Search
29. Klik `Download`, pilih `Download as CSV`
30. Verifikasi berkas CSV terunduh memuat baris DD-F2 `E2801160600002054D8A6001`
31. Kirim permintaan Delete DD-F2 langsung ke server memakai sesi Total Control Client Free (klien HTTP, tanpa lewat UI)
32. Verifikasi permintaan ditolak 403 Forbidden
33. Verifikasi tag DD-F2 tetap ada (state data dibaca lewat kemampuan baca disediakan tim FE/BE)

### TC-GS-TAG-317: Downgrade ke Free: tag non-QR tidak dihapus, tetap ada namun tidak dapat diakses

34. Logout, lalu login sebagai Total Control Client Down
35. Buka Global Settings > TAG > Tab All
36. Verifikasi tag RFID tetap tercantum di registri
37. Verifikasi sel TAG Type tag RFID menampilkan ikon gembok
38. Hover ikon gembok tag RFID
39. Verifikasi tooltip `Upgrade to unlock`
40. Verifikasi tag QR dapat dikelola (menu baris tag QR tampil tanpa ikon gembok)
41. Verifikasi kartu counter tidak tampil

### TC-GS-TAG-318: Plan berbayar (Growth/Professional/Enterprise): perilaku identik tanpa pembatasan antar-tier

42. Untuk setiap client pada tabel "TC-318" di bawah (Client A, Client Professional, Client Enterprise), lakukan langkah 43 sampai 50

| Client | Akun |
|---|---|
| Client A (Growth) | Total Control Client A |
| Client Professional | Total Control Client Professional |
| Client Enterprise | Total Control Client Enterprise |

43. Logout, lalu login sebagai Total Control client pada baris tabel
44. Buka Global Settings > TAG > Tab All
45. Verifikasi tombol `+ Activate TAG` tampil
46. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
47. Ketik `356938035643001` di input entri manual, klik `Add`
48. Klik `Submit`
49. Klik `Submit` pada dialog `Submit Activation`
50. Verifikasi toast sukses `Success, TAG has been activated.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 7d). Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian P-5: TC-316 butir c (Delete langsung 403, langkah 31 sampai 33) adalah satu-satunya request langsung di spec ini dan objek-uji ringan kelas a; berada di spec plan tier karena permukaan dan akun Client Free yang sama (butir b P-5).
- Langkah 42 sampai 50 adalah perulangan tiga client: Untuk setiap baris tabel "TC-318" (langkah 43 sampai 50), 8 langkah x 3 client = 24 langkah setelah ekspansi; tiap `Verifikasi` tetap satu per klausa.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 8, 15, 17, 25, 28, 34, 35 (login dan membuka), langkah 8, 15, 34, 43 (ganti akun eksplisit, S-07), dan penutupan popup. Langkah 26 sampai 28 (Search lalu `(←)`) adalah bagian Expected b TC-316 ("Search ... dapat membaca baris"); langkah 29 sampai 30 untuk "Download ... dapat membaca baris".
- Alasan spec melewati sekitar 35 langkah (nominal 50, ekspansi 66): semua blok satu kelas harness (h, state tenant/plan tier) dengan satu butir kelas a ringan (P-5 b); tiap blok berdiri sendiri dengan akun berbeda dan Step ganti akun eksplisit, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna (bagian 3 konvensi kasus (b)). Langkah 42 sampai 50 diulang per client dengan parameter di tabel. Spec mencampur blok bukan pembuat data (TC-315, TC-316, TC-317, TC-318: hanya membaca dan menekan aksi yang ditolak atau tidak ada) dengan satu aksi tulis sukses per client pada TC-318 (Activate) dan satu Delete langsung yang ditolak: semuanya satu kelas (h, plan tier) pada permukaan dan akun yang berbagi Seed; blok TC-318 yang membuat data ada di akhir dan pembersihannya mengikuti Prerequisites, sehingga kegagalan keras di blok itu tidak menutupi hasil blok baca.
- Temuan untuk QA:
  - TC-315 langkah 2 ("Ulangi sebagai Manage TAG (Update)") tidak menyebut akun Manage TAG (Update) di Client Free; Pre-setup TC hanya memuat Manage TAG (Update) untuk Client A. Akun ditulis "disediakan tim FE" (S-13).
  - TC-316 Expected b ("Search dan Download tetap dapat membaca baris tersebut") tidak mendefinisikan asersi Download; spec mengasersi berkas CSV memuat Code DD-F2 (butuh pembaca CSV).
  - TC-316 tidak menyebut identifier tag NFC, BLE, GPS warisan walau judulnya menyebut "RFID, NFC, BLE, GPS warisan"; Pre-setup Client Free hanya memuat DD-F1 (QR) dan DD-F2 (RFID). Spec hanya menguji DD-F2.
  - TC-317 tidak menyebut identifier tag RFID dan QR Client Down, serta cara teramati "tag QR dapat dikelola"; spec memakai menu baris tag QR tampil tanpa ikon gembok (kurang konkret).
  - TC-318 Expected "UI identik" tidak punya baseline pembanding (Q-8); spec mengasersi hanya tombol Activate tampil dan toast sukses pada tiap plan. TC-318 Precondition menyebut login Client A tetapi langkah mencakup tiga client.
  - Post Condition semua TC bernilai `-`.
