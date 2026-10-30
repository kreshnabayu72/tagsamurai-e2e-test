---
id: TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih
title: "Create Division: Screening Popup, Aksesibilitas, Clear Field, dan Tutup Bersih"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-31
  - TC-GS-DIV-32
  - TC-GS-DIV-63
  - TC-GS-DIV-64
  - TC-GS-DIV-67
coverage:
  web: automated
---

# Create Division: Screening Popup, Aksesibilitas, Clear Field, dan Tutup Bersih

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku popup Create di browser.
- Aktor yang dimodelkan lewat payload izin mock: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`. Sesi dibangun dari payload mock sehingga tidak ada login nyata dan tidak membutuhkan password. Bila spec dijalankan terhadap backend nyata, kredensial memakai `Spectra.env.GS_TC_PASSWORD`.
- Kebutuhan mock (seluruh endpoint yang dipanggil tab Division pada kondisi tes; endpoint dan event mengikuti LLD Division `API/low-level-design.md` L159, L256, L347; API pendukung di luar sumber modul disediakan tim FE):
  - Respons sesi/profil dan payload izin (disediakan tim FE): Total Control dengan capability Manage user and role lengkap (Read, Create, Update, Delete) sehingga `[+ Division]` tampil.
  - Respons `POST /v2/iam/divisions/list`: 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury) berurutan A-Z, sehingga tab Division dan tombol `[+ Division]` tampil.
  - Respons `POST /v2/iam/divisions/check-availability` saat mengetik Name dan Code: `Finance` dinyatakan sudah dipakai sesuai data Pre-setup, nilai lain tersedia.
  - Stream SSE tab Division (PRD `division.md` bagian Sync + Realtime; LLD L159, L256, L347 hanya menyebut event `division.created`, `division.updated`, `division.deleted` tanpa payload dan tanpa path endpoint, sehingga path stream disediakan tim FE): koneksi stream di-mock tetap terbuka dan tidak mengirim event apa pun selama spec, sehingga tidak ada refetch atau perubahan data tabel.
  - `POST /v2/iam/divisions` (Create) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit data yang valid; langkah 13 men-submit Name kosong yang diblokir di sisi klien).
- Data: tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup. Nilai uji `Energy Management`, `Finance`, dan `fin@` hanya diketik dan tidak pernah disimpan.
- Guided Tooltip: respons flag `guided_tooltip_seen_gs-division` (disediakan tim FE) di-mock true supaya walkthrough otomatis tidak menutupi layar.
- Kemampuan teknis: navigasi keyboard (Tab, Enter, Esc) dan pembacaan fokus elemen serta atribut ARIA (`aria-required`, `aria-describedby`).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` dengan respons mock di atas.
- State global: tidak ada yang diubah. Hook `after` hanya melepas mock.

## Test Steps

### TC-GS-DIV-31: Screening Popup Create Division (Expected a TC-GS-DIV-32 diasersi pada form yang sama)

1. Klik `[+ Division]`
2. Verifikasi kursor otomatis fokus pada input Division Name saat modal terbuka
3. Verifikasi Header: Title `Create Division`
4. Verifikasi Header: icon close `[✕]`
5. Verifikasi Body: field `Division Name *` dengan placeholder `Enter division name`
6. Verifikasi Body: field `Code` dengan placeholder `Enter code, or leave blank to auto-generate`
7. Verifikasi Body: Helper text Code selalu tampil `Letters, numbers, hyphens, underscores, and dots only`
8. Verifikasi Body: checkbox `Stay on this form after submitting` unchecked secara default
9. Verifikasi Footer: tombol `[Clear Field]` bergaya text, primary
10. Verifikasi Footer: tombol `[Submit]` bergaya filled, success
11. Verifikasi Footer: kedua tombol rata kanan
12. Verifikasi tidak ada tombol `[Cancel]`

### TC-GS-DIV-32: Accessibility Popup Create Division: fokus awal, aria, focus trap, Esc

13. Klik `[Submit]` dengan Division Name kosong
14. Verifikasi field Division Name memiliki `aria-required="true"`
15. Verifikasi error field Division Name terhubung lewat `aria-describedby`
16. Tekan Tab berulang melewati seluruh elemen modal
17. Verifikasi fokus keyboard tidak keluar dari modal (focus trap)
18. Tekan Esc
19. Verifikasi modal tertutup
20. Verifikasi dialog Unsaved Changes tidak muncul karena form kosong

### TC-GS-DIV-63: Tidak ada live preview Code hasil auto-generate saat Code kosong

21. Klik `[+ Division]`
22. Isi Division Name `Energy Management`
23. Verifikasi field Code tetap kosong dengan placeholder `Enter code, or leave blank to auto-generate`
24. Verifikasi tidak ada nilai Code yang terisi otomatis sebelum Submit

### TC-GS-DIV-64: Tombol Clear Field mengosongkan field dan mereset error tanpa dialog

25. Centang `Stay on this form after submitting`
26. Ganti Division Name dengan `Finance`
27. Isi Code `fin@`
28. Tunggu error inline tampil
29. Klik `[Clear Field]`
30. Verifikasi Division Name kosong
31. Verifikasi Code kosong
32. Verifikasi border error hilang
33. Verifikasi pesan error inline hilang
34. Verifikasi modal tetap terbuka
35. Verifikasi dialog Unsaved Changes tidak muncul
36. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
37. Tutup modal dengan `[✕]` (form kosong setelah `[Clear Field]`)

### TC-GS-DIV-67: Menutup form Create yang kosong tidak memunculkan dialog Unsaved Changes

38. Klik `[+ Division]` (form baru yang bersih)
39. Klik icon close `[✕]`
40. Verifikasi modal langsung tertutup
41. Verifikasi dialog Unsaved Changes tidak muncul

## Notes

- Mode: mock. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Daftar mock: `POST /v2/iam/divisions/list`, `POST /v2/iam/divisions/check-availability`, dan stream SSE tab Division (event `division.created`, `division.updated`, `division.deleted` menurut LLD L159, L256, L347; path stream disediakan tim FE, mock tidak mengirim event); `POST /v2/iam/divisions` (Create) tidak boleh terpanggil. Respons sesi/profil, menu, dan flag `guided_tooltip_seen_gs-division` disediakan tim FE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (41 langkah) karena lima TC screening popup Create berada di satu kelas harness (screening UI, mock) dan Expected Result TC-GS-DIV-31, TC-GS-DIV-32, dan TC-GS-DIV-64 memuat banyak klausa yang masing-masing diverifikasi; tiga pembukaan form (langkah 1, 21, 38) menutup form sesuai jumlah kejadian menutup, dan tiap blok berdiri sendiri.
- Pembukaan form ada tiga: pembukaan pertama untuk TC-GS-DIV-31 dan TC-GS-DIV-32 (screening, aksesibilitas, ditutup dengan Esc); pembukaan kedua untuk TC-GS-DIV-63 dan TC-GS-DIV-64 (form yang sama: TC-GS-DIV-63 mengetik Name lalu TC-GS-DIV-64 melanjutkan dengan mengganti Name dan mengisi Code, sehingga menghemat satu pembukaan; ditutup lewat `[✕]` pada langkah 37); pembukaan ketiga (form baru) untuk TC-GS-DIV-67 supaya penutupan bersih tidak bercampur dengan sisa state `[Clear Field]` (prinsip 6 konvensi).
- Urutan TC sumber diubah: TC-GS-DIV-32 dijalankan pada form yang sama dengan TC-GS-DIV-31. Expected a TC-GS-DIV-32 (fokus awal) diasersi di langkah 2 sebelum langkah yang mengubah fokus (bagian 8b butir 5); langkah 2 TC-GS-DIV-32 ("Perhatikan elemen yang mendapat fokus") adalah verifikasi fokus pada langkah 2 spec ini.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 37 (tutup modal TC-GS-DIV-64 lewat `[✕]`; form kosong tidak dirty sehingga tidak ada dialog). Langkah 38 (`Klik [+ Division]`, form baru) adalah langkah 1 TC-GS-DIV-67, bukan penghubung.
- Langkah 13 men-submit Name kosong: submit diblokir di sisi klien, tidak ada data tercipta, dan form tetap kosong sehingga Esc pada langkah 18 menutup modal tanpa dialog (Expected d TC-GS-DIV-32).
- Temuan untuk QA:
  - TC-GS-DIV-32 Expected b tidak menyebut teks pesan error Name kosong; spec hanya mengasersi atribut `aria-required` dan `aria-describedby`.
  - TC-GS-DIV-64 langkah 4 ("Tunggu error inline tampil") tidak menyebut field dan teks error. Data Uji memakai Name `Finance` (nama Division Pre-setup, berpotensi error duplicate) dan Code `fin@` (simbol terlarang); sumber error yang tampil tidak dinyatakan, sehingga kemunculan error tidak diasersi dan hanya dijadikan pemicu.
  - TC-GS-DIV-64 langkah 1 sampai 3 meminta form baru; spec melanjutkan form TC-GS-DIV-63 dan mengganti Name dengan `Finance` (langkah 26) agar tidak menambah pembukaan form.
  - TC-GS-DIV-67 mensyaratkan form baru yang kosong; sesuai bagian 3 prinsip 6 konvensi form pasca `[Clear Field]` tidak dihitung bersih sehingga dibuka form ketiga.
