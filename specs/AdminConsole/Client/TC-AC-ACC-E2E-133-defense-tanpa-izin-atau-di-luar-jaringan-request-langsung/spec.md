---
id: TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung
title: "Defense-in-depth: Request Langsung Tanpa Permission atau di Luar Jaringan Ditolak Server (Resend, Toggle BYO, Suspend, Delete, Change Partner)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-172
  - TC-AC-ACC-252
  - TC-AC-ACC-962
  - TC-AC-ACC-980
  - TC-AC-ACC-201
  - TC-AC-ACC-232
  - TC-AC-ACC-181
coverage:
  web: automated
---

# Defense-in-depth: Request Langsung Tanpa Permission atau di Luar Jaringan Ditolak Server (Resend, Toggle BYO, Suspend, Delete, Change Partner)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun, Step ganti akun eksplisit):

| Blok | Akun | Email | Env password | TC |
|---|---|---|---|---|
| 1 | Active-Read A-04 (Manage active client: Read, exact-match Area Jakarta) | `activeReadJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_READ_PASSWORD` | 172, 252, 962, 980 |
| 2 | Active-Delete-Only A-07 | `activeDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_DELETE_PASSWORD` | 201 |
| 3 | Archived-Update-Only A-09 | `archivedUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ARCHIVED_UPDATE_PASSWORD` | 232 |
| 4 | Distributor Total Control A-13 (PT Distribusi Nusantara) | `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` | `AC_CLIENT_DIST_TC_PASSWORD` | 181 |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga data tidak berubah): C-LIF-16 `PT Aktif Plus Menunggu` (FAMS Active, Default User Not Yet Activated); C-01 `PT Sejahtera Abadi` (Active, toggle BYO Disabled; target TC-AC-ACC-252 dan 201); C-02 `PT Teknologi Maju` (FAMS Grace) dan C-08 `PT Mulai Esok` (FAMS Pending) untuk TC-AC-ACC-962; C-FX12-1 `PT Suspend Langganan Aktif` (Suspended, FAMS Active) dan C-FX12-4 `PT Suspend Menunggu Persetujuan` (Suspended, FAMS Waiting for Approval) untuk TC-AC-ACC-980; C-04 `PT Karya Abadi` (Archived) untuk TC-AC-ACC-232; C-13 `PT Ganti Mitra` (hanya CV Mitra Sejati, dalam jaringan PT Distribusi Nusantara) untuk TC-AC-ACC-181. Partner pembanding: `CV Mitra Lestari` (dalam jaringan) dan `CV Mitra Timur` (jaringan PT Distribusi Timur).
- Kemampuan teknis (kelas a): klien HTTP/Fixture BE yang mengirim request langsung ke server memakai token sesi API milik aktor blok yang sedang login (disediakan tim FE/BE; sesi API tidak dihitung sebagai sesi web, dinyatakan di `suite.md`); membaca nilai toggle BYO dan keberadaan Client lewat Fixture BE/List.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Read

#### TC-AC-ACC-172: Resend tanpa Update pada Manage active client: Hidden dan ditolak server

1. Ketik Search `PT Aktif Plus Menunggu`, tekan Enter, klik Company Name `PT Aktif Plus Menunggu` lalu lihat section Default User
2. Verifikasi section Default User menampilkan badge "Not Yet Activated"
3. Verifikasi `[Resend Activation Email]` Hidden
4. Kirim request Resend Activation Email langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Aktif Plus Menunggu`
5. Verifikasi request ditolak server dengan respons 403 Forbidden

#### TC-AC-ACC-252: Toggle tanpa Update Manage active client: Hidden dan ditolak server

6. Klik breadcrumb "Client", ketik Search `PT Sejahtera Abadi`, tekan Enter, klik Company Name `PT Sejahtera Abadi`
7. Verifikasi toggle "Allow Self-Purchased Device Activation" Hidden
8. Kirim request langsung ke server lewat klien HTTP (tanpa melalui browser) set "Allow Self-Purchased Device Activation" ke Enabled untuk `PT Sejahtera Abadi`
9. Verifikasi request ditolak server dengan respons 403 Forbidden
10. Verifikasi nilai toggle `PT Sejahtera Abadi` tetap Disabled

#### TC-AC-ACC-962: Delete langsung tanpa permission Delete untuk Client yang terkena constraint: ditolak server dengan respons 403, bukan respons 422 (D-03 atau D-14)

11. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Teknologi Maju`
12. Verifikasi request ditolak server dengan respons 403 Forbidden
13. Klik breadcrumb "Client", klik sub-tab Active, ketik Search `PT Teknologi Maju`, tekan Enter
14. Verifikasi baris `PT Teknologi Maju` tetap tampil di sub-tab Active
15. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Mulai Esok`
16. Verifikasi request ditolak server dengan respons 403 Forbidden
17. Ganti isi Search dengan `PT Mulai Esok`, tekan Enter
18. Verifikasi baris `PT Mulai Esok` tetap tampil di sub-tab Active

#### TC-AC-ACC-980: Delete langsung untuk Client Suspended berriwayat tanpa permission Delete: ditolak izin (403) lebih dulu, bukan penolakan constraint 409

19. Ambil token sesi aktif milik Active-Read (hasil login Precondition a)
20. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Langganan Aktif` memakai token sesi tersebut, tanpa melalui UI
21. Verifikasi respons HTTP 403 Forbidden (ditolak izin lebih dulu), bukan 409 Conflict
22. Verifikasi body respons tidak memuat data Client
23. Klik sub-tab Suspended, ketik Search `PT Suspend Langganan Aktif`, tekan Enter
24. Verifikasi baris `PT Suspend Langganan Aktif` tetap tampil di sub-tab Suspended
25. Kirim permintaan HTTP ke endpoint Delete Client dengan ID `PT Suspend Menunggu Persetujuan` memakai token sesi yang sama, tanpa melalui UI
26. Verifikasi respons HTTP 403 Forbidden (ditolak izin lebih dulu), bukan 409 Conflict
27. Verifikasi body respons tidak memuat data Client
28. Ganti isi Search dengan `PT Suspend Menunggu Persetujuan`, tekan Enter
29. Verifikasi baris `PT Suspend Menunggu Persetujuan` tetap tampil di sub-tab Suspended

### Blok 2: Active-Delete-Only

30. Ganti akun: logout lalu login sebagai Active-Delete-Only A-07

#### TC-AC-ACC-201: Suspend tanpa Update Manage active client ditolak (bypass FE)

31. Kirim request Suspend langsung untuk `PT Sejahtera Abadi`
32. Verifikasi request ditolak server
33. Ketik Search `PT Sejahtera Abadi`, tekan Enter
34. Verifikasi `PT Sejahtera Abadi` tetap berstatus Active di sub-tab Active

### Blok 3: Archived-Update-Only

35. Ganti akun: logout lalu login sebagai Archived-Update-Only A-09

#### TC-AC-ACC-232: Delete tanpa permission Delete sesuai sub-tab ditolak (bypass)

36. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk Client `PT Karya Abadi` (Archived)
37. Verifikasi request ditolak server dengan respons 403 Forbidden
38. Klik sub-tab Archived, ketik Search `PT Karya Abadi`, tekan Enter
39. Verifikasi baris `PT Karya Abadi` tetap tampil di sub-tab Archived

### Blok 4: Distributor

40. Ganti akun: logout lalu login sebagai Distributor Total Control A-13

#### TC-AC-ACC-181: Distributor tidak dapat menambah Partner di luar jaringannya

41. Ketik Search `PT Ganti Mitra`, tekan Enter, klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`
42. Klik `[+ Add Partner]`
43. Verifikasi opsi memuat "CV Mitra Lestari"
44. Verifikasi opsi tidak memuat "CV Mitra Timur"
45. Tutup dropdown dengan klik area kosong di dalam dialog, lalu klik `[✕]` pada header dialog
46. Kirim request langsung ke server lewat klien HTTP (tanpa melalui browser) untuk menambah Partner "CV Mitra Timur" pada `PT Ganti Mitra`
47. Verifikasi request ditolak server dengan respons 403 Forbidden

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: ketujuh TC adalah kelas a dengan Expected berupa respons API dan state data; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`. Request langsung tidak melewati browser, sehingga asersi hanya kode respons dan state data (bagian 8b butir 1); request dikirim lewat klien HTTP (Sesi API aktor, `suite.md`) dan tidak ada toast atau dialog yang diasersi.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas tujuh TC satu kelas harness (kelas a, request langsung ditolak oleh server) dengan empat akun berbeda; ganti akun lewat Step eksplisit sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras; semua request ditolak sehingga tidak ada data yang diubah.
- Langkah penghubung (tanpa awalan Verifikasi): ganti akun (langkah 30, 35, 40), Search dan navigasi ke baris/Detail target (R-16), langkah 13 dan 17 (membaca keberadaan Client lewat List), dan langkah 45 (menutup dropdown dan dialog bersih sebelum request langsung).
- Asersi tambahan yang dicatat (S-03): langkah 10 (nilai toggle tetap Disabled) tidak ada di Expected TC-AC-ACC-252 dan ditambahkan sebagai asersi state data atas penolakan request langsung (bagian 8b butir 1).
- Post Condition TC-AC-ACC-172, 252, 962, 980, 201, 232, 181: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-201 tidak menyebut kode status penolakan dan tidak menyebut Client target; Expected hanya "Ditolak server; status tidak berubah". Spec memakai C-01 `PT Sejahtera Abadi`, mengasersi "ditolak server" dan status tidak berubah lewat List pada langkah 34.
  - TC-AC-ACC-181 tidak menyebut Client dalam jaringan; spec memakai C-13 `PT Ganti Mitra`.
